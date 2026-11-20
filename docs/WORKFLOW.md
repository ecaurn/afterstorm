# Deux machines à états

- **audit** : inventaire → vérification
- **vérification** : sources ciblées et outil fonctionnel → conception
- **conception** : graphe local et script → tranche
- **tranche** : deux parcours du pilote testés → campagne
- **campagne** : événements joués → médias
- **médias** : quota atteint → reprise ; inventaire complet → tests
- **tests** : écart → corrections ; zéro écart → livraison
- **corrections** : contrôle de non-régression → tests
- **blocage** : fichier ou source indisponible → consigner puis reprendre au dernier état vérifié
- **livraison** : archive, preuves et bilan
- **lecture** : choix → contrôle de scène et destination
- **enquête** : erreur → indice ou nouvel essai ; deux indices → assistance
- **décision** : effet déduit du journal → sauvegarde → destination selon parcours
- **carnet** : lecture sans mutation → retour
- **finPilote** : relecture/partie exportée/nouveau parcours sur confirmation

Reprise de production : relire `.project/etat.json`, contrôler les médias avec `scripts/validation.py`, exécuter le build et les tests. Ne pas confondre fin du pilote et livraison finale. La reprise de partie dérive la scène du journal : aucun coût n’est rejoué à l’ouverture du carnet.

Lot 2 : le point de fin n’est plus un test fixé à cinq décisions mais la longueur de la route. Le carnet est en lecture seule. Les points de chapitre nécessitent une confirmation avant remplacement. En reprise, ne pas régénérer les fichiers listés comme valides dans le registre. Pas d’archive, de PDF ou de nouvelle capture PNG.

Lot 3 : sélection de preuves → comparaison locale → correction ou décision → sauvegarde → conclusion distincte. Le point de chapitre remplace une partie seulement après confirmation. Point de reprise de production : après F13-02, suivre le graphe documenté plutôt que l’ordre des numéros.
