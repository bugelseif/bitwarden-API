$exclude = @("venv", "bitbot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bitbot.zip" -Force