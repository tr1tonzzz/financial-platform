"""Render via the canonical document rasterizer using hidden Word conversion on Windows.
The workspace runtime has no bundled LibreOffice. No user-installed LibreOffice is used.
"""
import importlib.util, subprocess, os
from pathlib import Path
skill=Path('C:/Users/admin/.codex/plugins/cache/openai-primary-runtime/documents/26.909.12148/skills/documents')
spec=importlib.util.spec_from_file_location('canonical_docx_render',skill/'render_docx.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
poppler='C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin'
os.environ['PATH']=poppler+os.pathsep+os.environ['PATH']
def convert(doc_path,user_profile,convert_tmp_dir,stem,verbose):
    pdf=Path(convert_tmp_dir)/(stem+'.pdf')
    env=os.environ.copy();env['PROPOSAL_RENDER_INPUT']=str(Path(doc_path).resolve());env['PROPOSAL_RENDER_OUTPUT']=str(pdf.resolve())
    command=r"""
$ErrorActionPreference='Stop'
$proposalWord=$null
$proposalDocument=$null
try {
 $proposalWord=New-Object -ComObject Word.Application
 $proposalWord.Visible=$false
 $proposalWord.DisplayAlerts=0
 $proposalDocument=$proposalWord.Documents.Open($env:PROPOSAL_RENDER_INPUT,$false,$true)
 $proposalDocument.ExportAsFixedFormat($env:PROPOSAL_RENDER_OUTPUT,17)
} finally {
 if($null -ne $proposalDocument){$proposalDocument.Close(0);[void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($proposalDocument)}
 if($null -ne $proposalWord){$proposalWord.Quit();[void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($proposalWord)}
}
"""
    proc=subprocess.run(['powershell','-NoProfile','-NonInteractive','-Command',command],env=env,capture_output=True,text=True,timeout=90)
    log=proc.stdout+proc.stderr
    if proc.returncode or not pdf.exists():return '',log
    return str(pdf),'Converted read-only DOCX with hidden Microsoft Word; '+log
module.convert_to_pdf=convert
if __name__=='__main__':module.main()
