$encoding = [System.Text.Encoding]::Default.BodyName
if ($encoding -eq "utf-8") {
    .\setup_env_utf8.ps1
} else {
    .\setup_env_utf8_bom.ps1
}