@echo off
echo ========================================
echo     PUSH FINAL VERS GITHUB
echo ========================================
echo.
cd /d "E:\09. LOGICIELS\GITHUB\ERP_AI-main"

echo Statut actuel:
git status --short

echo.
echo ========================================
echo IMPORTANT: Creez d'abord votre TOKEN
echo ========================================
echo.
echo 1. Allez sur: https://github.com/settings/tokens
echo 2. Generate new token (classic)
echo 3. Cochez [x] repo
echo 4. Generate token
echo 5. COPIEZ le token (ghp_xxxxxxxx)
echo.
echo ========================================
echo.
set /p ready="Avez-vous votre token pret? (o/n): "

if /i "%ready%"=="o" (
    echo.
    echo Envoi vers GitHub...
    echo Entrez vos identifiants quand demande:
    echo.
    git push -u origin main
    
    if %errorlevel% eq 0 (
        echo.
        echo ========================================
        echo SUCCES! Fichiers envoyes sur GitHub!
        echo https://github.com/ConstructoAI/ERP_AI
        echo ========================================
    ) else (
        echo.
        echo ========================================
        echo Si ca n'a pas fonctionne, essayez:
        echo.
        echo git push -u origin main --force
        echo.
        echo Ou dans Git Bash:
        echo git push https://USERNAME:TOKEN@github.com/ConstructoAI/ERP_AI.git main
        echo ========================================
    )
) else (
    echo.
    echo Creez d'abord votre token sur GitHub
)

echo.
echo Appuyez sur une touche pour fermer...
pause >nul