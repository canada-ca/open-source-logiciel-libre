# Guide de contribution aux logiciels libres

La [Directive sur la gestion des technologies de l’information](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=15249&section=procedure&p=C#appC), Annexe C, fournit les procédures obligatoires pour l’évaluation de l’architecture intégrée. Celles-ci seront utilisées par le Comité d’examen de l’architecture ministérielle et le Comité d’examen de l’architecture intégrée du GC en tant que cadre d’évaluation pour les initiatives numériques pour assurer que tous les sous-organismes du GC adhèrent à une seule direction numérique cohérente.

Cette stratégie s’harmonise avec les [Normes numériques](https://www.canada.ca/fr/gouvernement/systeme/gouvernement-numerique/normes-numeriques-gouvernement-canada.html) et l’exigence C.2.3.8 des [Procédures obligatoires pour l’évaluation de l’architecture intégrée](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=15249#claC.2.3.8), qui prévoient que tous les codes sources personnalisés doivent être publiés sous une licence de logiciel libre appropriée.

À ce titre, il est recommandé, pour les ministères, de contribuer à la collectivité toute modification au code source apportée au logiciel libre tiers, que ce soit à l’interne par les employés du GC ou par l’intermédiaire de contrats d’approvisionnement.

## Il y a de nombreuses façons de contribuer

Les collectivités de sources ouvertes sont menées par une vaste gamme de contributions. Un code qui fixe les bogues ou met en place des fonctionnalités de valeur est évidemment très important, mais des contributions qui ne sont pas un code, comme rédiger ou modifier les documents, ou présenter des demandes de fonctionnalités et des rapports de bogues, sont également très appréciées. Même simplement appuyer la contribution des autres ou exprimer un intérêt à la demande de fonctionnalité d’un autre, peut être une précieuse contribution.

Les étapes à suivre pour que le GC contribue un code dans les collectivités de logiciels libres sont les suivantes :

1. [Vérifier la licence des logiciels libres](#vérifier-la-licence-des-logiciels-libres)
2. [Vérifier les processus et politiques de contribution](#vérifier-les-processus-et-politiques-de-contribution)
3. [Approbations supplémentaires](#approbations-supplémentaires)
4. [Contribuer au projet](#contribuer-au-projet)
5. [Contribuer par l’intermédiaire des services professionnels](#contribuer-par-l’intermédiaire-des-services-professionnels)
6. [Publier les contributions indépendamment de l’acceptation en amont](#publier-les-contributions-indépendamment-de-l’acceptation-en-amont)

## Vérifier la licence des logiciels libres

Le GC peut contribuer à tous les logiciels ayant une [licence approuvée par Open Source Initiative](https://opensource.org/licenses) ou une [licence de logiciels gratuits de Free Software Foundation](https://www.gnu.org/licenses/license-list.html).

Si une licence pour un logiciel développé ouvertement est sous une autre licence, il faut consulter un conseiller juridique afin de préciser si les contributions sont recommandées.

## Vérifier les processus et politiques de contribution

Certains projets peuvent avoir des politiques précises pour la contribution de code (accord de licence des contributeurs, certificat d’origine du développeur) de même que des processus (modèles, plateformes, etc.). Avant de présenter une contribution, les employés devraient bien comprendre les processus et les politiques de contribution au projet. Les employés devraient ensuite veiller à ce que les approbations déléguées répondent à ces exigences.

### Accord de licence des contributeurs

Les accords de licence des contributeurs (ALC) sont des contrats que certains responsables de projet exigent que les contributeurs externes signent avant d’accepter leurs contributions. Ces contrats pourraient contenir diverses clauses, y compris les exemples suivants :

* Le contributeur externe confirme que le travail d’origine (la contribution) est son propre travail et peut donc légalement le partager avec le projet.
* Le droit d’auteur de la contribution doit être transféré aux responsables du projet.
* Les droits de brevets sont accordés aux responsables du projet pour les besoins de ce projet.
* Autres

Les contrats pouvant être complexes et contenir de nombreuses clauses différentes, il est vivement recommandé de consulter un avocat avant d’accepter ces obligations contractuelles supplémentaires.

En général, ce n’est pas un problème de contribuer à un projet qui a un ALC en place, mais une analyse supplémentaire est une pratique exemplaire. Certains projets s’éloignent de ces contrats complexes pour éliminer l’obstacle qu’ils créent autour des contributions externes en faveur du certificat d’origine du développeur.

### Certificat d’origine du développeur

Un certificat d’origine du développeur (COD) est considéré comme une façon de dire aux responsables du projet qu’en présentant cette contribution le contributeur confirme qu’il a le droit de le faire.

Il s’agit habituellement d’ajouter « signé par : contributor@email.com » dans la présentation du code.

Contrairement au ALC, si vous avez le droit de présenter une contribution, un COD ne devrait pas poser de problème comme vous devriez déjà avoir obtenu les approbations appropriées pour contribuer au projet. Voir [Approbations supplémentaires](#approbations-supplémentaires).

## Approbations supplémentaires

Si, pour une raison ou une autre, les approbations ministérielles déléguées ne respectent pas les exigences de contribution tierce, les employés devraient contacter leur superviseur pour savoir comment obtenir les approbations supplémentaires requises. Les ministères devraient définir des critères spécifiques pour l’approbation de contributions à source ouverte et les décrire clairement aux employés.

### Temps

Certains ministères peuvent instituer des directives ou des politiques énonçant que les employés doivent obtenir l’accord de leur gestionnaire pour passer du temps public à contribuer aux logiciels libres. Cela ne devrait pas être destiné à réduire la contribution à source ouverte, mais seulement de permettre la priorisation des besoins opérationnels; la politique par défaut devrait être d’encourager la contribution aux projets à source ouverte utilisés par le GC.

### Ministère

Semblable aux données ouvertes ou aux renseignements ouverts visés par la [Directive sur le gouvernement ouvert](https://www.tbs-sct.gc.ca/pol/doc-fra.aspx?id=28108), la publication du code source sous une licence de logiciel libre exige les approbations du bon ministère ou organisme.
Cette personne peut varier en fonction du ministère et la délégation devrait être encouragée au niveau le plus bas possible pour encourager la contribution aux projets de logiciels libres tiers.

## Contribuer au projet

### S’identifier en tant qu’employé du gouvernement du Canada

En vue de contribuer, il peut être nécessaire d’établir un compte avec le site ou la plateforme où le projet auquel vous voulez contribuer est hébergé. Cela devrait indiquer clairement que vous êtes un employé du gouvernement du Canada puisque vous contribueriez en tant que tel. S’il y a une option de voir votre organisme listé sur le projet, il serait avantageux de le faire.

À l’heure actuelle, il est recommandé que les employés utilisent leur nom au complet et l’adresse courriel du gouvernement du Canada pour toutes les contributions de code aux dépôts publics tout en agissant dans l’exercice de leurs fonctions ou de leur emploi comme il s’agit du principal moyen d’identifier leur travail. Certains services vous permettent d’énumérer plusieurs adresses courriel, d’autres peuvent vous demander de créer un nouveau compte pour les contributions officielles.

**Remarque** : cette disposition est liée à la [Loi sur les inventions des fonctionnaires](https://laws-lois.justice.gc.ca/fra/lois/P-32/TexteComplet.html#h-3), article 3. Des éclaircissements supplémentaires sur les moyens de s’identifier en tant qu’employé du GC sans exiger l’adresse de courriel dans les engagements devront être recherchés pour faciliter le processus et votre organisme peut déjà disposer de ses propres directives sur ce sujet.

### Présenter les changements

Pour apporter des changements dans les logiciels libres, collaborez avec la collectivité et présentez vos changements en amont, ce qui signifie au projet d’origine, afin d’assurer que vos modifications sont appuyées par les futures mises à jour. De cette façon, vos changements aideront à améliorer le logiciel pour tous ceux qui l’utilisent, mais vous veillerez également à rester conforme avec le projet d’origine et à ne pas avoir à conserver une version distincte du code source.

Contribuer à un tiers devrait être fait conformément au modèle de gouvernance du projet, si un tel modèle est présent.

## Contribuer par l’intermédiaire des services professionnels

Si votre ministère aimerait tirer parti des services professionnels pour contribuer à des projets tiers, consultez [Obtenir les droits de personnaliser le code dans les contrats](publication-code-source-ouvert.md#obtenir-les-droits-de-personnaliser-le-code-dans-les-contrats).

## Publier les contributions indépendamment de l’acceptation en amont

Qu’un ensemble de changements soit accepté ou non en amont en tant que contribution, les changements doivent quand même être publiés conformément au [Guide pour la publication de code source libre](publication-code-source-ouvert.md).

La publication permet en amont, dans le projet d’origine, de tenir compte des changements ultérieurement et permet à des tiers de tenir compte des changements, indépendamment du moment où le projet d’origine le fait ou s’il le fait.

Les changements non acceptés par le projet d’origine devraient tout de même être notés dans les forums du projet d’origine lorsque cela est possible et approprié, pour que les tiers qui pourraient être intéressés par ces changements aient un moyen de les découvrir.
