$webhookUrl = "https://hook.us2.make.com/2pbta4s12hgf6yow6m89sfiw3wwfm90h"

try {
    Invoke-RestMethod -Uri $webhookUrl -Method Post
    Add-Content -Path "C:\Users\Justin\OneDrive\Documents\Coding\Pinterest\test_log.txt" -Value "$(Get-Date) Webhook Sent"
} catch {
    Add-Content -Path "C:\Users\Justin\OneDrive\Documents\Coding\Pinterest\test_log.txt" -Value "$(Get-Date) Webhook Failed: $($_.Exception.Message)"
}
