# Guide pour la publication du code source libre

La [Directive sur la gestion des technologies de l’information](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=15249&section=procedure&p=D#appC), annexe C, fournit les procédures obligatoires pour l’évaluation de l’architecture intégrée, qui seront utilisées par les Conseils d’examen de l’architecture (CEA) et le CEA intégré du gouvernement du Canada (GC) en tant que cadre d’évaluation pour examiner les initiatives numériques visant à assurer que le GC agit comme unique entreprise et à assurer l’harmonisation ministérielle avec l’orientation numérique du GC.

Ceux-ci s’harmonisent avec les [normes numériques](https://www.canada.ca/fr/gouvernement/systeme/gouvernement-numerique/normes-numeriques-gouvernement-canada.html) et l’exigence aux points C.2.3.8 et C.2.3.9.5 des [Procédures obligatoires pour l’évaluation de l’architecture intégrée](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=15249#claC.2.3.8), qui prévoient que tous les codes sources doivent être publiés sous une licence libre appropriée et lorsqu’il ne l’est pas, il doit être partagé au sein du gouvernement du Canada.

Par conséquent, il est recommandé que, lorsqu’ils ont le droit de le faire, les ministères publient tout le code source en tant que logiciel libre, que la solution logicielle soit (i) acquise en tant que logiciel libre, (ii) mise au point par les employés du GC à l’interne ou (iii) acquise au moyen des conditions des contrats d’approvisionnement où des conditions de licence appropriées ont été négociées.

Lorsque la divulgation du code en général n’est pas appropriée ou possible, on recommande de commencer par le partage interne du code source à tous les ministères, dans la mesure où les conditions de la licence applicable autorisent ce partage. Il faut veiller à ce que la licence accordée au Canada ne limite pas la distribution de ce code à certains ministères utilisateurs. Cela permettra de rendre le code source prêt à être rendu public à titre de logiciel libre, lorsque le Canada aura reçu ce droit.

Voici les étapes à suivre pour publier le code source du GC :

1. [Demander les approbations](#demander-les-approbations)
2. [Obtenir les droits de personnaliser le code dans les contrats](#obtenir-les-droits-de-personnaliser-le-code-dans-les-contrats)
3. [Considérer les conséquences de sécurité](#considérer-les-conséquences-de-sécurité)
4. [Choisir une licence des logiciels libres](#choisir-une-licence-des-logiciels-libres)
5. [Choisir un dépôt de code source](#choisir-un-dépôt-de-code-source)
6. [Ajouter des fichiers recommandés](#ajouter-des-fichiers-recommandés)
7. [Publier une ancienne application](#publier-une-ancienne-application)
8. [Travailler dans un environnement ouvert](#travailler-dans-un-environnement-ouvert)

## Demander les approbations

### Équipe

La Directive sur la gestion des TI appuie la norme numérique n° 3 : Travailler ouvertement par défaut, au moyen des [Procédures obligatoires pour l’évaluation de l’architecture intégrée (C2.3.8)](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=15249&section=procedure&p=C#appC).

Partagez de façon ouverte les données probantes, les résultats de recherche et les prises de décisions. Rendez accessibles toutes les données de nature non sensible, tous les renseignements et tout le nouveau code source conçu dans le cadre de la prestation de services, afin que le monde extérieur puisse se les échanger et les réutiliser sous une licence ouverte.

Conformément à la vision pour un gouvernement ouvert, les équipes devraient par défaut considérer adapter leurs processus afin de développer sous source libre dès le début des projets afin de réduire les coûts indirects liés à la publication ultérieure de leur code source.

Il a également été constaté que cela améliore la qualité du code développé et encourage la collaboration.

### Ministère

Semblable aux données ouvertes ou aux renseignements ouverts visés par la [Directive sur le gouvernement ouvert](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=28108), la publication du code source sous une licence libre exige les approbations du bon ministère ou organisme.
Cette personne peut varier en fonction du ministère et la délégation devrait être encouragée au niveau le plus bas possible pour encourager la publication du code source libre.

## Obtenir les droits de personnaliser le code dans les contrats

La [Politique sur les droits de propriété intellectuelle](https://www.ic.gc.ca/eic/site/068.nsf/fra/00005.html) issus de marchés conclus avec l’État d’Innovation, Sciences et Développement économique Canada (ISDE) stipule que l’entrepreneur est propriétaire des droits de propriété intellectuelle de base créée à la suite d’un contrat d’achat de l’État. Toutefois, lorsque l’utilisation prévue par l’État de la propriété intellectuelle peut être satisfaite par le biais d’accords de licence, elle a la possibilité de rechercher la ou les licence (s) nécessaire (s), qu’elle soit large ou restreinte.

Dans le cadre de la discussion avec l’unité des services juridiques de l’institution et de l’examen de la politique applicable, il convient de noter que le [Guide des clauses et conditions uniformisées d’achat](https://achatsetventes.gc.ca/politiques-et-lignes-directrices/guide-des-clauses-et-conditions-uniformisees-d-achat/5/K/K3030C/2) de Services publics et Approvisionnement Canada (SPAC) renferme des clauses pour demander une [Licence concernant le matériel protégé par des droits d’auteur](https://achatsetventes.gc.ca/politiques-et-lignes-directrices/guide-des-clauses-et-conditions-uniformisees-d-achat/5/K/K3030C/2), qui peut utiliser les clauses des contrats si le ministère ou l’organisme veut que les droits d’auteur sur l’œuvre appartiennent à l’entrepreneur, mais souhaite obtenir une licence pour exercer tous les droits compris dans les droits d’auteur.

Les ministères ou organismes peuvent publier le code développé à la suite d’un contrat d’approvisionnement de l’État sous une licence libre, où ces droits ont été accordés au Canada. Le contrat d’approvisionnement pourrait également exiger à l’organisme contractant d’être responsable de la publication du code source sous une licence libre acceptable ou de contribuer directement au logiciel libre existant à l’aide de la licence de ce projet, et ces clauses seraient efficaces si convenues par le fournisseur.

## Considérer les conséquences de sécurité

### Développer un logiciel ouvertement

* Conserver les données sensibles comme les justificatifs d’identité en lieu sûr et séparément du code source.
* Éviter d’entreposer des clés et d’autres documents de nature délicate dans des systèmes non approuvés à cette fin.
* L’examen du code augmente la probabilité de détecter les bogues, les vulnérabilités en matière de sécurité et réduit le risque d’engager des données sensibles.
* Mettre en œuvre des mesures de contrôle suffisantes pour la prévention des changements non autorisés ou accidentels comme signer le code et établir des droits d’accès pour les utilisateurs des dépôts de code.
* Élaborer des stratégies d’atténuation et de processus pour régler les incidents liés à la sécurité.
* Intégrer les pratiques de sécurité dans vos processus et méthodes quotidiennes.
* Tirer parti des outils et services pour automatiser la recherche de vulnérabilités connues, de clés secrètes possibles et de renseignements personnellement identifiables.

## Choisir une licence des logiciels libres

Lorsque le projet fait partie d’une communauté plus vaste de logiciels libres, telle que des plug-ins, des modules, des extensions ou des travaux dérivés de logiciels libres existants, il est vivement recommandé d’utiliser la licence généralement utilisée par la communauté.

Lorsque le projet est démarré par le GC lui-même et qu’il n’est pas lié à une communauté externe, le choix de la licence libre doit être fondé sur les licences des éléments (bibliothèques et cadres tiers) que vous utiliserez et les résultats escomptés.

### Licences permissives recommandées

#### MIT

**Quand utiliser** des petits projets et des scénarios simples.
**Texte de licence** https://opensource.org/licenses/MIT

#### Apache 2.0

**Quand utiliser** de plus grands projets de logiciels qui utilisent Apache 2.0 parce qu’il fournit un octroi de brevets.
**Texte de licence** http://www.apache.org/licenses/LICENSE-2.0.txt

### Licences réciproques recommandées

« GPL 3.0 ou version ultérieure », « LGPL 3.0 ou version ultérieure » et « AGPL 3.0 ou version ultérieure » font référence à la version 3 des licences avec la note « ou version ultérieure ». Il ne s’agit pas d’un engagement envers la version future des licences.

#### « GPL 3.0 ou version ultérieure »

**Quand utiliser** le logiciel
**Texte de licence** https://www.gnu.org/licenses/gpl-3.0.txt

#### « LGPL 3.0 ou version ultérieure »

**Quand utiliser** les bibliothèques
**Texte de licence** https://www.gnu.org/licenses/lgpl-3.0.txt

#### « AGPL 3.0 ou version ultérieure »

**Quand utiliser** des applications et des services Web
**Texte de licence** https://www.gnu.org/licenses/agpl-3.0.txt

### Installer une licence

Afin d’appliquer le code source, ajouter le texte de la licence choisie à un fichier LICENCE.txt dans le dossier source du projet. Voir [Ajouter des fichiers recommandés](#ajouter-des-fichiers-recommandés). Vous pouvez aussi ajouter le texte de la licence directement dans l’un de vos fichiers de code source, mais en le rendant clairement disponible à la source de votre projet, vous le rendez plus facile à trouver pour les personnes qui le cherchent et certaines plateformes de collaboration peuvent automatiquement afficher votre licence sur l’interface Web.

Si plusieurs licences peuvent être appliquées, choisir une licence qui correspond à l’objectif du projet et ses interactions avec d’autres projets. Cela tend à dépendre de la décision d’appliquer une licence réciproque ou permissive.

#### Permissive

**Bénéficiaires du lancement du logiciel libre** Tout le monde : maximise la portée des utilisateurs en aval et a un vaste appel de tout le secteur privé... une plus grande flexibilité pour que les utilisateurs finaux, les développeurs et les entreprises puissent réutiliser le logiciel comme bon leur semble, y compris dans le cadre de logiciels commerciaux.

**Bénéficiaires des modifications du code en aval** Toute la communauté, mais seulement lorsque l’entreprise, l’organisme ou un développeur individuel choisit d’apporter des modifications en vertu de la licence permissive.

**Complexité des licences** Souvent courte, simple et compréhensible (par exemple MIT).

**Interopérabilité** Le code d’une licence permissive peut être inclus dans les projets visés par des licences réciproques, d’autres licences permissives ou des licences propriétaires.

#### Réciproque

**Bénéficiaires du lancement du logiciel libre** Tout le monde : Mais uniquement dans la mesure où ces personnes diffusent leur logiciel selon les mêmes modalités d’octroi de licence dont elles bénéficient. Approprié dans les cas où il est important de recevoir les changements en aval, ou lorsqu’il est important de veiller à ce que les travaux fondés sur un investissement initial restent des logiciels libres... peut également mettre l’accent sur les autres entreprises du secteur privé qui fournissent des services et du soutien.

**Bénéficiaires des modifications du code en aval** Toute la communauté chaque fois où une entreprise, un organisme ou un développeur individuel distribue les modifications ou contribue aux modifications sous la licence réciproque.

**Complexité des licences** Jargon juridique relativement long et complexe (par exemple AGPL 3.0).

**Interopérabilité** Un code de licence réciproque ne peut généralement pas être inclus dans un projet en vertu d’une autre licence.

#### Principales différences

Les différences parmi la gamme de licences réciproques GPL illustrent comment le type de distribution et l’étendue de l’intégration interagissent pour déterminer dans quelles circonstances une obligation réciproque s’applique, comme le montre le tableau suivant.

##### Œuvre dérivée de l’original

Œuvre dérivée de l’original – Distribution du code source
GPLv3 : Oui - LGPLv3 : Oui - AGPLv3 : Oui
Œuvre dérivée de l’original – Fourniture d’un accès sur un réseau informatique
GPLv3 : Non - LGPLv3 : Non - AGPLv3 : Oui

##### Œuvre dérivée avec liens vers l’original seulement

Œuvre dérivée avec liens vers l’original seulement – Distribution du code source
GPLv3 : Oui - LGPLv3 : Non - AGPLv3 : Oui
Œuvre dérivée avec liens vers l’original seulement – Fourniture d’un accès sur un réseau informatique
GPLv3 : Non - LGPLv3 : Non - AGPLv3 : Oui
Collection, y compris l’original non modifié.
Collection, y compris l’original non modifié – Distribution du code source
GPLv3 : Non - LGPLv3 : Non - AGPLv3 : Non
Collection, y compris l’original non modifié – Fourniture d’un accès sur un réseau informatique
GPLv3 : Non - LGPLv3 : Non - AGPLv3 : Non

### Droits sortants

Il faut toujours s’assurer que les droits sortants associés à la licence choisie ne dépassent pas les droits entrants de tout élément de logiciel utilisé dans le code source. Par exemple, il ne serait pas légalement possible de publier un projet sous une licence MIT (permissive) si les éléments du logiciel utilisés dans celui-ci ont été initialement publiés sous une licence GPL3 (réciproque).

### Droits d’auteur

La [Loi canadienne sur le droit d’auteur (article 2)](https://laws-lois.justice.gc.ca/fra/lois/c-42/page-4.html#h-7) prévoit que, lorsqu’un travail est, ou a été, préparé ou publié par ou sous la direction ou le contrôle de Sa Majesté ou tout ministère, le droit d’auteur sur le travail appartient, sous réserve de tout accord avec l’auteur, à Sa Majesté. Cela s’applique à tout code source développé par des employés du gouvernement du Canada.
Cependant, les employés du gouvernement du Canada ont des [Droits moraux](https://laws-lois.justice.gc.ca/fra/lois/c-42/page-4.html#h-8) et comme l’auteur d’un travail a le droit à l’intégrité du travail et le droit d’être associé au travail à titre d’auteur par nom ou sous un pseudonyme ainsi que le droit à l’anonymat.

### Identification appropriée du droit d’auteur du gouvernement du Canada

Selon l’article des [Demandes de droit d’auteur de la Couronne](https://www.canada.ca/fr/patrimoine-canadien/services/demandes-droit-auteur-couronne.html) trouvé sur Canada.ca, la structure suivante devrait être appliquée pour l’avis de droit d’auteur du gouvernement du Canada.

Droit d’auteur (c) Sa Majesté la Reine du chef du Canada, représentée par la ministre de (nom légal du ministère), (année de publication).
Remplacer le (nom légal du ministère) et (année de publication) avec l’information appropriée.

Cet avis devrait être ajouté au fichier LICENCE dans votre projet. Voir [Ajouter des fichiers recommandés](#ajouter-des-fichiers-recommandés).

## Choisir un dépôt de code source

Les dépôts de code source recommandés pour le code source libre du gouvernement du Canada sont les suivants :

* GitLab
* GitHub
* framagit
* Bitbucket

Le gouvernement du Canada a également un dépôt interne de code source à la disposition de tous les ministères et organismes.

* GCcode (interne au gouvernement du Canada seulement)

### Organismes

Les ministères et les organismes sont libres de choisir la plateforme qui convient le mieux à leurs besoins opérationnels, mais leurs projets devraient, dans la mesure du possible, être tous regroupés sous un organisme ou un groupe unique. Cela aiderait la découvrabilité de vos projets, mais aussi contribuerait à augmenter les possibilités de collaboration.

### Système de contrôle des versions

Le système de contrôle des versions recommandé pour le code libre du GC est Git. On encourage également les ministères à utiliser Git pour gérer leur code source à l’interne.

## Ajouter des fichiers recommandés

Avant d’être publié, le code source devrait inclure ce qui suit :

* un fichier LICENCE (voir [Choisir une licence des logiciels libres](#choisir-une-licence-des-logiciels-libres)) contenant une copie de la licence sous laquelle le code source est publié;

Par défaut, un projet sans une licence libre appliquée serait seulement publié dans le cadre du droit d’auteur de la Couronne.

**Remarque** : La licence libre peut être intégrée directement dans le code source, mais il est fortement recommandé de la mettre dans un fichier LICENCE distinct à la source du répertoire de votre projet.

De plus, les points suivants sont recommandés comme pratique exemplaire :

* Un fichier README.md fournissant de l’information sur le projet, comment l’utiliser et de la documentation sur le projet.
  * Il est également recommandé que ce dossier soit bilingue pour accroître l’utilisation et la contribution au projet.
* Un fichier CONTRIBUTING.md expliquant la façon de contribuer à la réalisation du projet.
* Un fichier SECURITY.md expliquant la politique sur la sécurité, ainsi que les procédures de déclaration des vulnérabilités en matière de sécurité.
* Un fichier CODE_OF_CONDUCT.md expliquant les valeurs et l’éthique pour les employés du secteur public et pour le projet.

Des exemples de ces fichiers sont disponibles dans le [dépôt de modèles](https://github.com/canada-ca/template-gabarit).

## Publier une ancienne application

Publier une ancienne application peut sembler beaucoup de travail, mais c’est faisable et, en fait, un bon investissement si l’application continuera d’être utilisée à l’avenir. La documentation pourrait être améliorée au cours de la publication du projet pour aider à accroître les contributions de la communauté.

De plus, publier une ancienne application peut mener à sa réutilisation et à accroître le développement des contributions de la part des parties intéressées. Cela peut relancer le développement actif de l’application, en lui fournissant des fonctionnalités améliorées et des corrections de bogues.

Les risques de vulnérabilité existent déjà et la publier comme logiciel libre ne change pas leur état. Une façon de limiter ces risques est de ne pas fournir les configurations de la version de production.

Des outils d’analyse dotés de fonctionnalités avancées et des tests de sécurité doivent être envisagés pour aider les équipes de développement à accélérer le processus de révision et de nettoyage.

## Travailler dans un environnement ouvert

### Diffuser tôt, diffuser souvent

Il est recommandé que le code source soit publié aussitôt que possible dans le cycle de vie du projet pour éviter les frais de publication du code source plus tard dans le processus. Le dépôt du code source public est encouragé à être la seule source de vérité où les développeurs travaillent. La plus récente version du code ne signifie pas nécessairement que c’est la version déployée en production.

### Être aux commandes

Lorsque vous travaillez dans les équipes ouvertes, vous contrôlez toujours ce qui entre dans le code source et une occasion d’examiner les contributions des développeurs internes et externes. Les droits d’accès peuvent être configurés pour les référentiels afin que seuls les membres autorisés de l’équipe puissent accepter les modifications. D’autres peuvent distribuer la version modifiée de votre code, mais cela ne signifie pas que les modifications doivent être acceptées dans le cadre de votre code.

### S’identifier en tant qu’employé du gouvernement du Canada

Les employés devraient utiliser leur nom au complet et l’adresse courriel du gouvernement du Canada pour toutes les contributions de code aux répertoires publics tout en agissant dans l’exercice de leurs fonctions ou de leur emploi.

### Langues officielles

La [Politique sur les langues officielles](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=26160) ne s’applique pas au code source des logiciels (y compris les commentaires en ligne).
Cependant, les mêmes règles sur les LO comme toute autre application élaborée par le GC ou au nom du GC dans le passé devrait s’appliquer pour ce qui est de la documentation de l’utilisateur final, si le projet a été publié ou non comme logiciel libre.

### communauté

Établir une communauté accueillante peut influencer l’avenir et la réputation de votre projet. En offrant une expérience positive aux contributeurs et en leur facilitant les interactions avec l’équipe de projet, vous les encouragez à continuer de contribuer. Vous devez répondre aux questions, bogues et fusionner les demandes pour encourager les gens à continuer de vous aider.

Il est recommandé d’inclure un fichier README.md et un fichier CONTRIBUTING.md avec votre code source. Voir [Ajouter des fichiers recommandés]((#ajouter-des-fichiers-recommandés)).

### Accord de licence de contributeur

Les projets du gouvernement du Canada n’exigent pas d’accords de licence des contributeurs, mais reposent sur des licences de logiciel libre fournissant les conditions nécessaires. Les contributions sont faites sous la même licence sous laquelle le projet est publié et les auteurs conservent leurs droits d’auteur pour leurs contributions.

### Échange de ressources ouvertes

Il est vivement recommandé aux ministères d’ajouter un lien vers les dépôts de code source de leurs projets dans la [section de code source libre d’Échange de ressources ouvertes](https://canada-ca.github.io/ore-ero/fr/index.html). Cela permettra de rehausser la visibilité de tous les projets gérés par le GC et potentiellement accroître la collaboration.

Les directives sur la façon de mettre à jour les données peuvent être trouvées sur [GitHub](https://github.com/canada-ca/ore-ero/tree/master/_data#donn%C3%A9es-pour-l%C3%A9change-de-ressources-ouvert).
