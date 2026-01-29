---
description: Deploy or restart Cloudflare Tunnel for Castle Studio services
---

// turbo-all
1. 檢查雲端隧道配置檔 `/Users/paulchen2021/.cloudflared/castle.yml`。
2. 檢查目前是否有正在運行的 cloudflared 進程。
3. 如果有正在運行的進程，先將其終止。
4. 使用指定的配置檔重新啟動 Cloudflare Tunnel。

```bash
# 檢查並清理現有進程
ps aux | grep cloudflared | grep -v grep | awk '{print $2}' | xargs kill -9 2>/dev/null || true

# 啟動 Tunnel (背景執行)
nohup cloudflared tunnel --config /Users/paulchen2021/.cloudflared/castle.yml run ee8462b1-608a-420b-821c-6bd3c5831b79 > /Users/paulchen2021/.cloudflared/tunnel.log 2>&1 &
```
