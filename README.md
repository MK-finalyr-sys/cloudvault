# CloudVault

CloudVault is an S3-compatible object storage manager built on Vue 3, Hono, Cloudflare Workers, D1 and R2.

## Import
The GitHub Actions workflow `Import and white-label CloudVault` imports the original open-source FlareDrive Remastered application, applies CloudVault branding and commits the result. If it does not run automatically, open **Actions → Import and white-label CloudVault → Run workflow**.

## Deploy to Cloudflare
1. Create a new D1 database named `cloudvault`, a KV namespace, and an R2 bucket in your own Cloudflare account.
2. Replace `REPLACE_WITH_CLOUDVAULT_D1_ID` and `REPLACE_WITH_CLOUDVAULT_KV_ID` in `wrangler.jsonc` with the IDs Cloudflare gives you.
3. Keep `ALLOW_REGISTER` set to `false`. Set the `ADMIN_CREATE_TOKEN` Worker secret using `bunx wrangler secret put ADMIN_CREATE_TOKEN`.
4. Install Node.js 22+ and Bun; run `bun install`, `bun run drizzle:push` for local D1, then `bun run build`.
5. Apply production migrations using the upstream-documented `bun run drizzle:push-prod` after setting the Cloudflare account, API token and D1 database ID in your local environment. Do not commit credentials.
6. Run `bun run deploy` after authenticating Wrangler to your Cloudflare account. Create the first admin with the upstream `bun run user:create` command and a strong unique password. Configure the R2 bucket through the admin UI.

**Note:** This GitHub repository does not automatically provision Cloudflare resources or deploy. Verify imported source, image paths, build, and storage operations before public launch.

## Attribution
Based on [FlareDrive Remastered](https://github.com/project-epb/flaredrive-rev), licensed under MIT. Preserve the upstream `LICENSE` with original copyright notices. CloudVault branding is separate from upstream artwork.
