# Podpina pamiec Claude Code (folder memory/ w tym repo) pod sciezke,
# ktorej Claude Code szuka na TEJ maszynie. Dziala niezaleznie od litery dysku.
# Uruchom raz po sklonowaniu repo:   .\setup-maszyny.ps1

$repo = $PSScriptRoot
$memoryWRepo = Join-Path $repo "memory"

if (-not (Test-Path $memoryWRepo)) {
    Write-Host "BLAD: nie znaleziono folderu memory\ w repo ($memoryWRepo)." -ForegroundColor Red
    exit 1
}

# Claude Code robi nazwe folderu ze sciezki: dwukropki i backslashe -> myslniki
# G:\MARKA\ContentAI\CONTENT  ->  G--MARKA-ContentAI-CONTENT
$nazwaProjektu = $repo.Replace(':', '-').Replace([char]92, '-').Replace('/', '-')
$docelowy = Join-Path $env:USERPROFILE ".claude\projects\$nazwaProjektu"
$linkPamieci = Join-Path $docelowy "memory"

Write-Host "Repo:            $repo"
Write-Host "Nazwa projektu:  $nazwaProjektu"
Write-Host "Podpinam pod:    $linkPamieci"
Write-Host ""

New-Item -ItemType Directory -Path $docelowy -Force | Out-Null

$istniejacy = Get-Item $linkPamieci -ErrorAction SilentlyContinue
if ($istniejacy) {
    if ($istniejacy.LinkType -eq "Junction") {
        Write-Host "Junction juz istnieje - podmieniam na aktualny." -ForegroundColor Yellow
        (Get-Item $linkPamieci).Delete()
    } else {
        # Prawdziwy folder z pamiecia - nie kasuj, odstaw na bok
        $backup = "$linkPamieci`_backup_$(Get-Date -Format yyyyMMdd-HHmmss)"
        Move-Item $linkPamieci $backup
        Write-Host "Znalazlem prawdziwy folder pamieci - odstawilem go na: $backup" -ForegroundColor Yellow
        Write-Host "Sprawdz go pozniej, moga tam byc wpisy ktorych nie ma w repo." -ForegroundColor Yellow
    }
}

New-Item -ItemType Junction -Path $linkPamieci -Target $memoryWRepo | Out-Null

$liczba = (Get-ChildItem $linkPamieci -File -ErrorAction SilentlyContinue | Measure-Object).Count
if ($liczba -gt 0) {
    Write-Host ""
    Write-Host "GOTOWE. Pamiec podpieta, widocznych plikow: $liczba" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "UWAGA: junction powstal, ale nie widac plikow. Sprawdz recznie." -ForegroundColor Red
}
