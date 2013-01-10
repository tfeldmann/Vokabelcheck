python C:\PyInstaller\pyinstaller.py -w -i assets\icon.ico --onefile vokabelcheck.py
copy Endungen.txt dist /Y
cd dist
ren vokabelcheck.py Vokabelcheck.py
