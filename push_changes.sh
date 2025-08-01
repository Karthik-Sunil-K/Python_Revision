
FOLDER_NAME=$(grep '^FOLDER_NAME=' starter.sh | cut -d '=' -f2 | sed 's/^"//;s/"$//')

git add .
git commit -m "$FOLDER_NAME is added"
git push origin main
