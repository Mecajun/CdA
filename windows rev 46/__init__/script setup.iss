[Setup]
AppName=Controle de Acesso
AppVersion=1.0
DefaultDirName={pf}\Controle de Acesso
DefaultGroupName=Controle de Acesso
UninstallDisplayIcon={app}\Controle de acesso.exe
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Inno Setup Examples Output
[Languages]
Name: ptbr; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"
[Run]
Filename: "{sd}\Program Files\MySQL\MySQL Server 5.7\bin\mysql.exe"; Parameters: "-u root -padmin -e""CREATE DATABASE controledeacesso;""";
[Files]
Source: "__init__.exe"; DestDir: "{app}"
Source: "__init__.exe.manifest"; DestDir: "{app}"
Source: "_ctypes.pyd"; DestDir: "{app}"
Source: "_hashlib.pyd"; DestDir: "{app}"
Source: "_mysql.pyd"; DestDir: "{app}"
Source: "_socket.pyd"; DestDir: "{app}"
Source: "_ssl.pyd"; DestDir: "{app}"
Source: "bz2.pyd"; DestDir: "{app}"
Source: "gdiplus.dll"; DestDir: "{app}"
Source: "kernel32"; DestDir: "{app}"
Source: "logo.png"; DestDir: "{app}"
Source: "Microsoft.VC90.CRT.manifest"; DestDir: "{app}"
Source: "msvcm90.dll"; DestDir: "{app}"
Source: "msvcp90.dll"; DestDir: "{app}"
Source: "msvcr90.dll"; DestDir: "{app}"
Source: "msvcrt.dll"; DestDir: "{app}"
Source: "python27.dll"; DestDir: "{app}"
Source: "pywintypes27.dll"; DestDir: "{app}"
Source: "select.pyd"; DestDir: "{app}"
Source: "unicodedata.pyd"; DestDir: "{app}"
Source: "user32.dll"; DestDir: "{app}"
Source: "win32api.pyd"; DestDir: "{app}"
Source: "win32evtlog.pyd"; DestDir: "{app}"
Source: "wx._controls_.pyd"; DestDir: "{app}"
Source: "wx._core_.pyd"; DestDir: "{app}"
Source: "wx._gdi_.pyd"; DestDir: "{app}"
Source: "wx._misc_.pyd"; DestDir: "{app}"
Source: "wx._windows_.pyd"; DestDir: "{app}"
Source: "wxbase28uh_net_vc.dll"; DestDir: "{app}"
Source: "wxbase28uh_vc.dll"; DestDir: "{app}"
Source: "wxmsw28uh_adv_vc.dll"; DestDir: "{app}"
Source: "wxmsw28uh_core_vc.dll"; DestDir: "{app}"
Source: "wxmsw28uh_html_vc.dll"; DestDir: "{app}"

[Icons]
Name: "{group}\My Program"; Filename: "{app}\__init__.exe"
