@echo off
echo ========================================
echo     PUSH FINAL VERS GITHUB
echo ========================================
echo.
cd /d "E:\09. LOGICIELS\GITHUB\ERP_AI-main"

echo Statut Git actuel:
git status --short
echo.
echo ========================================
echo ETAPE 1: PREPARATION DU TOKEN
echo ========================================
echo.
echo Si vous n'avez PAS encore de token:
echo 1. Ouvrez: https://github.com/settings/tokens
echo 2. Generate new token (classic)
echo 3. Cochez [x] repo
echo 4. Generate token
echo 5. COPIEZ le token (ghp_xxxxxxxx)
echo.
pause

echo.
echo ========================================
echo ETAPE 2: ENVOI VERS GITHUB
echo ========================================
echo.
echo GitHub va vous demander:
echo - Username: Votre nom utilisateur
echo - Password: Collez votre TOKEN
echo.
echo Note: Le token n'apparait pas quand vous le collez (normal)
echo.

git push -u origin main

echo.
echo ========================================
if errorlevel 1 (
    echo ERREUR DETECTEE
    echo.
    echo Solutions possibles:
    echo 1. Verifiez votre token
    echo 2. Essayez cette commande dans Git Bash:
    echo    git push -u origin main --force
    echo.
    echo 3. Ou avec token directement:
    echo    git push https://USERNAME:TOKEN@github.com/ConstructoAI/ERP_AI.git main
) else (
    echo SUCCES! Fichiers envoyes!
    echo Verifiez sur: https://github.com/ConstructoAI/ERP_AI
)
echo ========================================
echo.
pause