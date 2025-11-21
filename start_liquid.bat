@echo off
echo Démarrage du serveur llama.cpp...

cd llama_cpp
.\llama-b6853-bin-win-cpu-x64\llama-server.exe --model ..\models\LFM2-350M-Q4_0.gguf --ctx-size 2048 --port 8080 --embedding --mlock --jinja

.\myenv\Scripts\activate