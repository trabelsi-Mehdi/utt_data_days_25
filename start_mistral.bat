@echo off
echo Démarrage du serveur llama.cpp...

cd llama_cpp
.\llama-b6853-bin-win-cpu-x64\llama-server.exe --model ..\models\Mistral-7B-Instruct-v0.3-abliterated-Q3_K_M.gguf --ctx-size 2048 --port 8080 --embedding --mlock

.\myenv\Scripts\activate