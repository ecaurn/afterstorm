# Moteur et capacités

HTML/CSS, modules JavaScript natifs, graphe JSON avec contrôles à l’exécution. Sans bibliothèque dans le navigateur. Pas de compilation TypeScript : les contraintes actuelles sont vérifiées par énumération de journaux. InkJS 2.4.0 et JSON exécutent un embranchement (`node tests/graph.cjs`). Ink conviendrait aux dialogues imbriqués ; le graphe direct donne aux variantes, médias et empreintes les mêmes identifiants inspectables sans interpréteur supplémentaire. Un seul moteur en production.

Node 20.20.2 ; versions de développement verrouillées. Build = copie sous `jeu/` (persistant). Tests sous `/fiction/`. Sonnage original : voix native Arena fr voice-00 sélectionnée ; MP3 mono 44,1 kHz, lus avec libsndfile et dans Chromium. Aucun besoin de Piper, FFmpeg, clé ou compte. Deux premiers essais = S01 et S02, conservés comme clips de production. Les autres MP3 ne sont pas prétendus contrôlés à l’oreille. Pas de musique ni d’effets ajoutés à ce lot. Les fichiers ne sont pas préchargés en bloc.

Le format 1 sauvegarde identifiant de parcours, décisions et aides. Recalcul des ressources sans effets de bord. Import contrôlé par rejouage, confirmation puis remplacement. La relecture ignore les choix. Aucune télémétrie. Licence de redistribution spécifique du modèle vocal et détails d’entraînement non fournis par l’outil : ne pas confondre accès et autorisation.

Défaut reproduit en test : après une requête audio interrompue, le second clic ne relançait pas toujours le média. Correction : remplacer l’instance en erreur avant relance. Régression passée dans tests/pilot.cjs.

## Reprise du lot 1
Pas de migration destructive : mêmes clés et schéma 1, ajout d’un mode facultatif (absence = Histoire). Les cinq décisions anciennes sont un préfixe valide des nouvelles routes. Les tests importent le fichier antérieur `tests/preuves/fin-B.json` sans l’écraser. Un journal fabriqué qui paie une action impossible est refusé. Les images sont contrôlées comme de véritables JPEG et les variantes comme fichiers MP3 individuels, sans conversion substitutive. Pour le prochain lot, étendre le suffixe des routes, jamais réinterpréter un choix ancien pour insérer une scène en milieu de parcours sans migration explicite.

Lot 3 : la sauvegarde v1 accepte un champ `indices` facultatif exclusivement au dossier actif. Identifiants bornés, sans doublons, maximum deux. Le log conserve ensuite la décision `pair`, non les tentatives ; la sélection transitoire est effacée après résolution. Les fichiers réels de fin du lot 2 restent des fixtures non modifiées. Le tableau agrandi utilise le même JPEG local ; aucune image dérivée ou capture créée. Voir `tests/lot3.cjs` et `tests/contraintes.cjs`.
