# Guide Installation Git sur Windows

## 1. Télécharger Git
- Allez sur https://git-scm.com/download/win
- Téléchargez le fichier .exe
- Lancez l'installation (gardez les options par défaut)

## 2. Configurer Git (une seule fois)
Ouvrez **Command Prompt** ou **PowerShell** et tapez :
```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
```

## 3. Cloner votre projet
```bash
cd E:\09. LOGICIELS\GITHUB
git clone https://github.com/[votre-username]/ERP_AI-main.git
```

## 4. Ajouter les nouveaux fichiers
```bash
cd ERP_AI-main
git add .
git status
```

## 5. Créer un commit
```bash
git commit -m "Ajout 120 postes de travail construction pour Render"
```

## 6. Pousser vers GitHub
```bash
git push origin main
```
(Il vous demandera vos identifiants GitHub)

## Alternative : Utiliser un Token
Si l'authentification par mot de passe ne fonctionne pas :
1. Allez sur GitHub → Settings → Developer settings → Personal access tokens
2. Créez un nouveau token avec les droits "repo"
3. Utilisez ce token comme mot de passe lors du `git push`