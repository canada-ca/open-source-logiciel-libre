# Guide d'utilisation de logiciels libres

La [Directive sur la gestion des technologies de l’information, annexe C](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=15249#appC), fournit les procédures obligatoires pour l’évaluation de l’architecture intégrée, qui seront utilisées par les Conseils d’examen de l’architecture (CEA) et le CEA intégré du gouvernement du Canada (GC) en tant que cadre d’évaluation pour examiner les initiatives numériques visant à assurer que le GC agit comme unique entreprise et à assurer l’harmonisation ministérielle avec l’orientation numérique du GC.

Celles-ci s’harmonisent avec les [Normes numériques](https://www.canada.ca/fr/gouvernement/systeme/gouvernement-numerique/normes-numeriques-gouvernement-canada.html) et [l’exigence C.2.3.8 des Procédures obligatoires pour l’évaluation de l’architecture intégrée](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=15249#claC.2.3.8) qui prévoient que, dans la mesure du possible, des logiciels libres soient utilisés en premier.

Les étapes à suivre pour que le GC utilise des logiciels libres sont les suivantes:

1. [Envisager activement et équitablement les logiciels libres](#envisager-activement-et-équitablement-les-logiciels-libres)
2. [Vérifier la propriété ou la licence libre](#vérifier-la-propriété-ou-la-licence-libre)
3. [Évaluer les options de soutien](#Évaluer-les-options-de-soutien)
4. [Utiliser les logiciels libres sans modification](#utiliser-les-logiciels-libres-sans-modification)
5. [Utiliser les logiciels libres avec modifications](#utiliser-les-logiciels-libres-avec-modifications)
6. [S’inscrire à l’Échange de ressources ouvertes](#s’inscrire-à-l’Échange-de-ressources-ouvertes)

## 1. Envisager activement et équitablement les logiciels libres

Il faut être conscient que les logiciels libres ne sont pas complètement gratuits, on doit donc tenir compte du coût total de possession (CTP) de la migration, y compris les coûts de sortie, de transition et de soutien.

### Être conscient du « Open Core » (cœur ouvert)

Une solution fondée sur un logiciel libre, mais qui nécessite l’utilisation d’éléments privés ne devrait pas être considérée comme un logiciel libre pour les besoins du présent guide.
Le modèle de développement « Open Core » est celui où les fournisseurs n’ouvrent que des parties de leur logiciel et entourent le reste d’éléments fermés, ainsi que le modèle où un utilisateur comme le Canada bonifie un logiciel propriétaire avec des logiciels libres.
Les versions « gratuites » de ces logiciels libres, souvent qualifiées d’éditions « communautaires », sont recommandées en premier.
Voir [Vérifier la propriété ou la licence des logiciels libres](#vérifier-la-propriété-ou-la-licence-des-logiciels-libres).

### Choisir des logiciels libres en priorité

Les procédures obligatoires pour l’évaluation de l’architecture intégrée voir ([l’annexe C de la Directive sur la gestion des technologies de l’information](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=15249#appC)) nécessitent une architecture d’application – pour une nouvelle technologie ainsi que pour la mise à niveau ou la migration de solutions existantes – afin de prioriser l’utilisation de logiciels libres de même que les normes ouvertes.
Ce faisant, on maximise la substituabilité et l’interopérabilité des éléments de logiciels et ouvre la voie à la création de solutions très souples.
Cela aide également à atténuer les risques importants liés au verrouillage (« lock-in ») et à des problèmes semblables.

Parfois, une solution libre satisfait la plupart des besoins des utilisateurs, mais exigerait des investissements supplémentaires pour développer une fonctionnalité manquante (voir le [Guide de contribution aux logiciels libres](contribution-logiciels-libres.md)).

Dans ces cas, cet investissement doit être considéré en pondérant le coût total de possession par rapport à ceux des autres solutions potentielles.

### Évaluation

Les mêmes facteurs qui s’appliquent à l’évaluation de l’ensemble de caractéristiques et de la maturité des logiciels propriétaires s’appliquent également aux logiciels libres.
D’autres critères devraient être évalués lors de l’évaluation des logiciels libres :

#### 1. Communauté d'utilisateurs

Une forte communauté d’utilisateurs participant à un projet permet aux gens de répondre aux questions, de procéder à la mise à l’essai du logiciel, de signaler les bogues, de suggérer des améliorations et de susciter un intérêt général pour le logiciel.
Examinez le dépôt de code public du logiciel et vérifiez la popularité du projet en regardant le nombre de « j’aime » et d’abonnés.
Vérifiez l’activité du projet par rapport aux utilisateurs en examinant les problèmes et le temps entre les réponses.

#### 2. Communauté de développeurs

Une forte communauté de développeurs ayant des antécédents de publication et une participation continue tend à démontrer que les correctifs et les améliorations aux logiciels se poursuivront à l’avenir.
Observez qui sont les principaux développeurs et qui appuie le projet et la communauté, comme un organisme sans but lucratif.
Vérifiez le moment du lancement du projet, le rythme selon lequel les versions sont sorties et les réponses aux demandes d'intégration de code provenant des contributeurs.

#### 3. Documentation

La documentation de l’utilisateur fournit des renseignements importants pour aider les utilisateurs à installer le logiciel et à utiliser ses fonctions.
La documentation technique fournit les exigences et les instructions pour l’installation, le développement, le déploiement et la configuration du logiciel.

#### 4. Évaluations de la sécurité

Bien que le code des logiciels libres soit vérifiable, cela ne signifie pas nécessairement qu’il est sécuritaire.
La qualité du code et le temps de réponse habituel pour corriger les lacunes de sécurité aident à indiquer le niveau de maturité de la sécurité du logiciel.
Comme pour tout logiciel, vous devriez maintenir les pratiques exemplaires et avoir un processus en place pour énumérer tous les paquets en utilisation de même que leur version afin de les corriger rapidement.

## 2. Vérifier la propriété ou la licence libre

Chaque fois que l’État envisage d’obtenir des logiciels sous licence libre, les ministères devraient examiner les modalités pour vérifier s’ils peuvent accepter et se conformer à celles-ci compte tenu de leur contexte opérationnel particulier.

Le logiciel est habituellement fourni « tel quel », ce qui signifie que la communauté n’acceptera pas la responsabilité ou ne fournira pas de compensation financière à l’État pour l’interruption de service, la perte de données ou la perte de confidentialité.
Par conséquent, vous devriez considérer le logiciel obtenu sous licence libre avec les mêmes objectifs de responsabilité que si vous l’aviez développé.

Tous les logiciels sous une [licence approuvée par la Open Source Initiative](https://opensource.org/licenses/alphabetical) ou la [Free Software Foundation](https://www.gnu.org/licenses/license-list.html#SoftwareLicenses) sont considérés comme des logiciels libres, et peuvent être utilisés par le GC [sans modification](#utiliser-les-logiciels-libres-sans-modification), dans la mesure du possible et conformément au présent guide.

Toutefois, si le logiciel doit être modifié, les considérations suivantes doivent être abordées avec les intervenants appropriés (c’est-à-dire, les utilisateurs finaux, les gestionnaires de projet et les services juridiques) et appliquées afin de déterminer les conditions de licence que le Ministère est disposé à approuver.

1. Y a-t-il des raisons qui empêcheraient la publication du code source modifié?
   * Non : sous réserve des considérations précitées, vous pouvez accepter toute licence approuvée OSI ou FSF.
   Voir [Utiliser les logiciels libres avec modifications](#utiliser-les-logiciels-libres-avec-modifications).
   * Oui : Voir 2.
2. L’application modifiée sera-t-elle utilisée comme une application Web?
   * Oui : sous réserve des considérations précitées, vous pouvez accepter toute licence approuvée OSI ou FSF, à l’exception des licences à forte réciprocité.
Voir [les licences à forte réciprocité](#licences-à-forte-réciprocité).
   * Non : Voir 3.
3. L’application modifiée sera-t-elle distribuée à l’externe, à l’extérieur du GC, soit le code source ou le code binaire?
   * Non : sous réserve des considérations précitées, vous pouvez accepter toute licence approuvée OSI ou FSF.
   * Oui : sous réserve des considérations précitées, vous pouvez accepter toute licence approuvée OSI ou FSF, à l’exception des [licences réciproques](#licences-réciproques).
   Utilisez seulement des [licences permissives](#licences-permissives).

Des consultations supplémentaires avec les services juridiques et les équipes d'ingénierie devraient être effectuées pour les scénarios où le logiciel libre est utilisé comme un élément d’un développement personnalisé (par exemple : lien dynamique ou statique, etc.) pour assurer la compatibilité de la licence.

### Licences populaires et largement utilisées

Ce qui suit constitue les listes de licences classées par catégorie permissive et réciproque.
Pour voir la liste complète, consulter les sites Web de la Open Source Initiative (OSI) et de la Free Software Foundation (FSF).

### Licences permissives

* Licence Apache
* Licence BSD
* Licence ISC
* Licence MIT

### Licences réciproques

* Eclipse Public License (EPL)
* Licence publique de l’Union européenne (EUPL)
* Licence publique générale GNU (GPL, LGPL et AGPL)
* Mozilla Public License (MPL)
* Open Software License (OSL)

## 3. Évaluer les options de soutien

L’utilisation d’un logiciel libre présente un modèle différent fondé sur des services de soutien plutôt que l’obtention d’une licence de logiciel.
Les deux principaux modèles de soutien pour les logiciels libres sont le soutien autonome, dans lequel l’équipe interne de TI du ministère ou de l’organisme est responsable de la maintenance et des interactions avec la communauté, ou le soutien professionnel.

### À l’interne

L’utilisation d’un modèle de soutien autonome exige que les équipes responsables :

* aient un processus approprié en place pour gérer l’évaluation et la mise en place des logiciels libres dans l’organisme;
* maintiennent et fassent le suivi des listes complètes de tous les logiciels utilisés, de quelle façon et par qui; et
* s’assurent que les mises à jour soient appliquées en temps opportun.

La communauté d'utilisateurs et de développeurs devrait être exploitée pour les questions de soutien général, ainsi que pour signaler les bogues, créer des demandes de fonctionnalités et des contributions de code.

Lorsqu’on utilise des éléments de logiciel à des fins de développement, de puissants outils et services peuvent être exploités par les équipes de TI afin d’automatiser, de faciliter et d’accélérer l’identification de ces éléments, y compris des logiciels libres.
Ces outils peuvent fournir des capacités d’analyse des vulnérabilités de sécurité connues ainsi que de respect des exigences juridiques.

Voir le [Guide de contribution aux logiciels libres](#contribution-logiciels-libres.md).

### Services professionnels

Il est possible de passer un contrat avec une entreprise de services professionnels pour assurer la maintenance, les mises à jour, la garantie et la responsabilité des logiciels libres.

Un autre scénario qui peut devenir récurrent serait de choisir un logiciel libre et utiliser la version communautaire, puis lancer ultérieurement un appel d’offres pour un soutien et un entretien professionnels.

Lorsque le développement personnalisé nécessite l’utilisation de développeurs sous contrat, il faut s’assurer que les droits appropriés sur le code source soient obtenus pour publier comme logiciel libre, conformément au [Guide de publication de code source libre](publication-code-source-libre.md).

## 4. Utiliser les logiciels libres sans modification

### Utiliser un logiciel libre sans modification n’exige pas que le code soit partagé

La configuration du logiciel, même par l’intermédiaire des fichiers de configuration, n’est pas considérée comme une modification.
Cela est également vrai pour les combinaisons de logiciels libres permettant de créer une solution ou un logiciel libre utilisé pour le développement et le déploiement.
Voir les exemples ci-dessous.

### Seul

Navigateur Web, suite de productivité, système d’exploitation et utilitaires (gestionnaire de fenêtre, environnement de bureau, éditeur de texte, console, etc.).

### Combinaison d’éléments

Applications et modules d’extension avec la base de données et le serveur Web.

### Développement et déploiement

Développement personnalisé à l’aide de langages de programmation libres et dépendances, serveur HTTP, système de gestion de base de données, plateforme de conteneur.

### Orientation

Pour le développement ou au moment de l'écriture du code source, consulter le [Guide de publication de code source libre](publication-code-source-libre.md).

## 5. Utiliser les logiciels libres avec modifications

### Utiliser un logiciel libre avec modifications n’est généralement pas considéré comme une distribution et n’exige pas que le code soit partagé

Les modifications apportées aux logiciels libres devraient quand même être partagées avec la communauté pour aider à assurer la viabilité de la solution.
Voir le [Guide de contribution aux logiciels libres](contribution-logiciels-libres.md).

Pour les cas où le partage des modifications est obligatoire, consulter les [répercussions à forte réciprocité](#répercussions-à-forte réciprocité).

### Ne pas faire d'embranchement (« fork ») du logiciel libre

### Dans la mesure du possible, utiliser des logiciels libres sans modification ou les contribuer au projet

Utiliser la configuration et personnaliser le logiciel avec des modules, des plugiciels ou des extensions et rendre ceux-ci disponibles à la communauté.
Voir le [Guide de publication de code source libre](publication-code-source-libre.md).

Il est facile de faire un embranchement (« fork ») d'un logiciel libre et de commencer à apporter des changements au code source.
Si un embranchement identique est créé, ce qui signifie prendre une copie du code source et maintenir une version séparée du projet d’origine, sachez que cela peut rendre les mises à jour et les correctifs de sécurité difficile à mettre en place.
L’équipe de développement qui a fait les changements sera responsable du maintien de ces changements indéfiniment à moins qu’ils ne soient contribués à la version en amont, qui est le projet d’origine à partir duquel le code source a été pris.

Pour apporter des changements aux logiciels libres, collaborer avec la communauté et présenter les changements en amont pour s’assurer qu’ils sont appuyés par les futures mises à jour, voir le [Guide de contribution aux logiciels libres](contribution-logiciels-libres.md).

**Remarque** : le terme « embranchement » au sens littéral peut être confondu avec le processus d'embranchement (clonage) des projets sur GitHub, GitLab et Bitbucket, qui est essentiel pour expérimenter et présenter des modifications au projet d’origine.

### Répercussions à forte réciprocité

Les licences à forte réciprocité considèrent que les logiciels accessibles par l’intermédiaire d’un réseau (comme Internet) sont de la distribution et le code source modifié doit être mis à la disposition des utilisateurs.
Voir les Guides sur la [Publication de code source libre](publication-code-source-libre.md) et sur la [Contribution aux logiciels libres](contribution-logiciels-libres.md)...

#### Licences à forte réciprocité

Les [licences approuvées de la Open Source Initiative](https://opensource.org/licenses/alphabetical) et de la [Free Software Foundation](https://www.gnu.org/licenses/license-list.html#SoftwareLicenses) contiennent les licences à forte réciprocité suivantes :

* GNU Affero General Public License (AGPL)
* Licence publique de l’Union européenne (EUPL)
* Open Software License (OSL)

## 6. S’inscrire à l’Échange de ressources ouvertes

Les ministères sont encouragés à ajouter tous les logiciels libres qu’ils utilisent à la section [Logiciels libres de l’Échange de ressources ouvertes](https://canada-ca.github.io/ore-ero/fr/index.html).

Le but de cette plateforme est d’aider à trouver les autres ministères qui ont utilisé avec succès les logiciels libres dans le cadre de l’environnement de production et créer des liens avec les communautés de logiciels libres autour d’eux.

Cela est également conforme à la norme numérique : Travailler ouvertement par défaut.

Les directives sur la façon de mettre à jour les données peuvent être trouvées sur [GitHub](https://github.com/canada-ca/ore-ero/blob/master/_data/README.md#donn%C3%A9es-pour-l%C3%89change-de-ressources-ouvert).