Get-ChildItem -Recurse -File | Where-Object { $_.LastWriteTime.Date -eq (Get-Date).Date } | ForEach-Object {
    $destPath = Join-Path -Path ".\day_7" -ChildPath $_.FullName.Substring((Get-Location).Path.Length + 1)
    $destDir = Split-Path $destPath
    if (-not (Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }
    Copy-Item $_.FullName -Destination $destPath -Force
}
