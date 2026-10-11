const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {chromium}=require(process.env.FAP_PLAYWRIGHT_PATH);
const root=path.resolve(__dirname,'../..'),dir=path.join(root,'docs/design-5-uc');
const manifest=JSON.parse(fs.readFileSync(path.join(dir,'manifest.json'),'utf8'));
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:process.env.FAP_CHROMIUM_PATH});
 try{
  const page=await browser.newPage({viewport:{width:1600,height:1300}}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.goto(pathToFileURL(path.join(dir,'index.html')).href);
  assert.equal(await page.locator('.screen-button').count(),10);
  const out=path.join(root,'_plan_render/design-5-uc');fs.mkdirSync(out,{recursive:true});
  const bounds=[];
  for(const screen of manifest.screens){
   const svg=fs.readFileSync(path.join(dir,screen.file),'utf8');assert(!/<image\b/.test(svg));assert(/<text\b/.test(svg));
   await page.locator(`[data-target="${screen.id}"]`).click();
   const view=page.locator('#view-'+screen.id);assert.equal(await view.isVisible(),true);
   const overflow=await view.locator('svg').evaluate(svg=>[...svg.querySelectorAll('text')].flatMap(n=>{const b=n.getBBox();return b.x<0||b.x+b.width>1441||b.y<0||b.y+b.height>1081?[{text:n.textContent,x:b.x,y:b.y,width:b.width,height:b.height}]:[]}));
   bounds.push({screen:screen.id,text_outside_frame:overflow});
   assert.equal(overflow.length,0,screen.id+' '+JSON.stringify(overflow));
   await view.screenshot({path:path.join(out,screen.id+'.png')});
  }
  await page.locator('[data-target="uc1"]').click();
  await page.locator('#view-uc1 [data-screen="source"]').first().click();assert.equal(await page.locator('#view-source').isVisible(),true);
  await page.locator('#view-source [data-screen="review"]').first().click();assert.equal(await page.locator('#view-review').isVisible(),true);
  await page.setViewportSize({width:390,height:844});
  await page.locator('[data-target="uc5"]').click();assert.equal(await page.locator('#view-uc5').isVisible(),true);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
  assert.deepEqual(errors,[]);
  const result={scope:'local design QA; not Figma canvas validation or application acceptance',screens:10,editable_text_vector_svg:10,checks:['SVG without image wrapper','10 screen switches','source/review walkthrough','text stays within SVG bounds','mobile horizontal canvas scroll without page overflow'],bounds,browser_errors:errors};
  fs.writeFileSync(path.join(dir,'validation.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
