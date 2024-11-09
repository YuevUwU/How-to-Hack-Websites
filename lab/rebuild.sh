LAB_PATH="$PWD"

cd $LAB_PATH/frontend/xss; sudo docker compose up -d --build --force-recreate
cd $LAB_PATH/logic-vulns; sudo docker compose up -d --build --force-recreate
cd $LAB_PATH/ssrf/SSRFrog; sudo docker compose up -d --build --force-recreate
cd $LAB_PATH/ssrf/preview-card; sudo docker compose up -d --build --force-recreate
cd $LAB_PATH/lfi; sudo docker compose up -d --build --force-recreate
cd $LAB_PATH/ssti; sudo docker compose up -d --build --force-recreate
cd $LAB_PATH/deserialization; sudo docker compose up -d --build --force-recreate
cd $LAB_PATH/sql-injection; sudo docker compose up -d --build --force-recreate
cd $LAB_PATH/cmd-injection; sudo docker compose up -d --build --force-recreate
