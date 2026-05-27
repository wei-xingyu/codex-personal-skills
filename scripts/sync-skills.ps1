param(
    [string]$CodexSkillsRoot = "$env:USERPROFILE\.codex\skills",
    [string[]]$SkillNames = @(
        "diagnose-answer-mode",
        "hatch-pet",
        "homework-pdf-answer",
        "pdf"
    )
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$targetRoot = Join-Path $repoRoot "skills"

New-Item -ItemType Directory -Force -Path $targetRoot | Out-Null

foreach ($skillName in $SkillNames) {
    if ($skillName.StartsWith(".")) {
        continue
    }

    $source = Join-Path $CodexSkillsRoot $skillName
    $target = Join-Path $targetRoot $skillName

    if (-not (Test-Path -LiteralPath $source)) {
        Write-Warning "Skip missing skill: $skillName"
        continue
    }

    if (-not (Test-Path -LiteralPath (Join-Path $source "SKILL.md"))) {
        Write-Warning "Skip non-skill folder: $skillName"
        continue
    }

    if (Test-Path -LiteralPath $target) {
        Remove-Item -LiteralPath $target -Recurse -Force
    }

    Copy-Item -LiteralPath $source -Destination $target -Recurse -Force
    Write-Host "Synced skill: $skillName"
}

Write-Host "Done. Review changes, then commit and push."

