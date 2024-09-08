server {
    listen 3000;
    server_name openinterest.ru;

    # Обслуживание статических файлов фронтенда
    location / {
        root /moex/frontend;
        index index.html;
        try_files $uri $uri/ /index.html;
    }
}