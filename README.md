# Après l’orage — Traverser, accueillir, restaurer

**Version jouable, couverture MP3 incomplète à l’échelle de la campagne.** Les deux parcours mènent du premier matin de Maëlle au fauteuil de Suzanne pendant l’attaque de Gog (E00–E11, puis E13). Pas de compte et pas de synthèse distante pendant une partie.

## Jouer ou reprendre
`python3 -m http.server 8000 --directory jeu`, puis ouvrir http://localhost:8000/. Sur la même origine, actualiser l’aperçu reprend la partie. Une sauvegarde complète du lot 1 ouvre directement la table des réserves. Pour découvrir les nouvelles scènes sans rejouer, Réglages → Point de chapitre : la photo sans légende → confirmer (exporter d’abord pour conserver la partie). Le point de chapitre fixe explicitement les décisions antérieures. Pour repartir : Réglages → Commencer un autre parcours, choisir Histoire ou Gestion puis A/B. Les repères documentaires et le carnet en lecture seule restent disponibles en cours de jeu.

| Mesure | Lot 3 cumulé |
|---|---:|
| Événements joués | 13 / 23 |
| Scènes distinctes | 19 / 54 |
| Monde nouveau | 0 / 26 planifiées |
| Enquêtes avec deux aides | 7 |
| JPG distincts | 19 |
| Blocs écrits / MP3 décodés | 27 / 27 |
| Variantes en plus d’un bloc par scène | 8 (dont trois résumés sensibles) |
| MP3 manquants sur texte intégré | 0 |
| Scènes prévues sans texte final ni narration | 35 |
| Borne inférieure de lots restants, 10 MP3/lot | 4 |
| Tests navigateur réussis | 28 |
| Journaux terminaux explorés, 2 routes × 2 modes | 14 336, aucune impasse |

Sept scènes, sept JPG et dix narrations nouvelles. Les anciennes fins du lot 2 reprennent en F08-01. Dix événements majeurs restent non joués : E12 et E14–E22. Non exécutés : parcours A et B jusqu’à E22 ; conséquence dans le monde nouveau ; écoute humaine ; accessibilité multi-navigateur manuelle. La carte évolutive, les projets de restauration, la musique originale et les effets restent à réaliser. Ce n’est pas une livraison finale.

## Fichiers et reproduction
- `jeu/` : build statique ; `index.html`, `style.css`, `app.js`, `engine.mjs` : sources. `npm ci && npm run build` pour reconstruire. Export : copier le dossier `jeu/` tel quel. Aucune nouvelle archive.
- `content/blocks.json` : textes approuvés. Pour réviser, modifier le bloc ; ne modifier ni le texte gelé ni l’empreinte dans le manifeste avant régénération effective du MP3. Une divergence désactive la lecture. Revalider le son et ses métadonnées après régénération. Publier le nouveau build seulement si la validation passe.
- `content/sources.json` : URL, passage, édition, consultation et date de mise en ligne si connue. Relire la publication, consigner la nouvelle compréhension, réviser les contraintes puis `content/coverage.json` et la scène. Une source retirée doit être signalée plutôt que remplacée silencieusement.
- `assets/art/`, `assets/voice/` : vrais fichiers locaux. `content/audio-manifest.json` : textes gelés, empreintes SHA-256, durées, tailles et niveaux. `content/plan-production.json` et `.project/media-ledger.json` : estimation des lots non écrits.
- `tests/preuves/` : captures historiques du premier lot, parties de test, résultats. Pour rejouer : `npm ci`, `npx playwright install --with-deps chromium`, `npm run build`, `npm test`, `node tests/graph.cjs`, `node tests/contraintes.cjs`. Validation des médias : Python avec pillow, soundfile, numpy, puis `python3 scripts/validation.py`. Le rapport distingue les défauts du pilote des événements encore absents.
- `docs/` : audit, matrice, couverture, recherche et droits. `.project/` : état et tâches de reprise. Données conservées dans le seul navigateur ; aucune collecte des croyances.

