
::for loop test
@echo off
for %%a in (00, 06,07,08,09,10,11,12,99) do (
cd %%a*
if exist README.md (echo "skipped "%%a) 
if not exist README.md (if exist README_en.md md-translator translate --src README_en.md --dest README.md --to zh)
cd ..
)
exit /b