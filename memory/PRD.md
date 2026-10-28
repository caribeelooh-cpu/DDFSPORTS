# PRD — Google Search Console Verification

## Original problem statement
Quero verificar meu site no Google Search Console. Preciso adicionar a meta tag de verificação do Google ao HTML da página inicial, dentro da seção `<head>`, sem alterar o design ou as funcionalidades do site.

## Architecture decisions
- Use CRA environment substitution in `frontend/public/index.html` so the verification token is available in the generated HTML without hardcoding it in source.
- Store the token as `REACT_APP_GOOGLE_SITE_VERIFICATION_TOKEN` through the secure environment mechanism.
- Keep the change limited to one metadata line inside `<head>`.

## Implemented
- Added one `meta[name="google-site-verification"]` entry to the homepage template.
- Confirmed `yarn build` succeeds and the production artifact contains a populated token with no placeholder.
- Confirmed the login page still loads visually and no design or functionality code was changed.

## Backlog
- P0: Publish/redeploy the current frontend build so the public root serves the new HTML.
- P1: Recheck the public root and submit the URL in Google Search Console.
- P2: None.

## Current status
- Source and local build are correct.
- The public and preview hosts currently serve an older/different HTML artifact with zero verification tags; publication remains unresolved.