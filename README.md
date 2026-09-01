# NAMU DESIGN 官网

NAMU DESIGN 官网源码。站点是无后端依赖的静态构建，包含中文、英文、亮色/暗色模式与响应式页面。

## 页面

- `/zh/`、`/en/`
- `/zh/info/`、`/en/info/`
- `/zh/work/fotile/`、`/en/work/fotile/`
- `/zh/work/farfetch-china/`、`/en/work/farfetch-china/`

## 本地构建

```sh
make build
make check
```

构建结果写入 `dist/`。生产服务器仅发布该目录；私钥和服务器凭据不得放入仓库。

## 部署

Nginx 配置位于 `deploy/`。生产部署采用 `/var/www/namu/releases/<版本>` 版本目录和 `/var/www/namu/current` 软链接，以便快速回滚。
