# Curl de teste com a integracao ao LiteLLM

curl --connect-timeout 5 --max-time 30 -s -X POST http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-gcn-nasa-master-key" \
  -H "Content-Type: application/json" \
  -d '{"model":"nasa-classifier","messages":[{"role":"user","content":"diga apenas: ok"}]}' | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['choices'][0]['message']['content'])"