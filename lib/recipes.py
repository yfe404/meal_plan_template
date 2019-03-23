"""
Mocking Recipe Service
"""
class RecipeService():

    def __init__(self):
        self.recipes = [
            {"calories": 650,
"proteins": 41,
"carbohydrates": 88,
"fats": 15,
"ingredients": [
{"name": "Fromage blanc 0%", "quantity": 250, "unit": "g"},
{"name": "Mangue", "quantity": 50, "unit": "g"},
{"name": "Myrtilles", "quantity": 50, "unit": "g"},
{"name": "Banane", "quantity": 80, "unit": "g"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
{"name": "Muesli (sans sucre ajouté)", "quantity": 65, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 2, "unit": "unit"},
],
"name": "Fromage blanc fruité", "steps": [
"Dans un grand bol: versez le fromage blanc et ajoutez les myrtilles et les framboises.",
"Coupez la mangue en dés et ajoutez les morceaux au fromage blanc.",
"Coupez la banane en tranches et ajoutez les morceaux au fromage blanc.",
"Ajoutez le muesli et mélangez.",
"Préparez les oeufs à part selon vos préférences, au plat, en omelette ou autre."
], "type": ["breakfast", "snack"]},




{"calories": 650,
"proteins": 42,
"carbohydrates": 75,
"fats": 20,
"ingredients": [
{"name": "Oeuf(s) entier(s)", "quantity": 3, "unit": "unit"},
{"name": "Blanc de poulet", "quantity": 60, "unit": "g"},
{"name": "Poivron", "quantity": 80, "unit": "g"},
{"name": "Champignons de Paris", "quantity": 80, "unit": "g"},
{"name": "Riz complet", "quantity": 100, "unit": "g"},
],
"name": "Omelette", "steps": [
"Dans un grand recipient: fouettez le oeufs. Vous pouvez ajouter du poivre et des épices selon vos préferences.",
"Dans un plat, coupez le blanc de poulet et les poivrons en dés.",
"Versez dans une poêle chaude votre mélange d'oeufs fouettés.",
"Ajoutez-y le poulet et les poivrons.",
"Laissez cuire jusqu'à ce que l'omelette soit prête.",
"Pour la cuisson du riz, référez-vous aux instructions présentes sur l'emballage (typiquement environ 10min dans une casserole d'eau bouillante)."
], "type": ['lunch', 'dinner']
},



{"calories": 600,
"proteins": 43,
"carbohydrates": 27,
"fats": 37,
"ingredients": [
{"name": "Fromage blanc 0%", "quantity": 100, "unit": "g"},
{"name": "Beurre de cacahuètes", "quantity": 30, "unit": "g"},
{"name": "Myrtilles", "quantity": 30, "unit": "g"},
{"name": "Framboises", "quantity": 30, "unit": "g"},
{"name": "Pomme", "quantity": 40, "unit": "g"},
{"name": "Graines de courge", "quantity": 20, "unit": "g"},
{"name": "Flocons de soja", "quantity": 60, "unit": "g"},
],
"name": "Fromage blanc fruité 2", "steps":[
"Dans un grand bol: versez le fromage blanc et le beurre de cacahuètes puis mélangez jusqu'à l'obtention d'un mélange homogène.",
"Ajoutez les myrtilles et les framboises.",
"Coupez la pomme en dés et ajoutez les morceaux au fromage blanc.",
"Ajoutez les flocons de soja et mélangez.",
"Ajoutez les graines de courge."
], "type": ["breakfast", "snack"]},



{"calories": 600,
"proteins": 32,
"carbohydrates": 36,
"fats": 36,
"ingredients": [
{"name": "Carottes râpées", "quantity": 50, "unit": "g"},
{"name": "Concombre", "quantity": 50, "unit": "g"},
{"name": "Feta", "quantity": 15, "unit": "g"},
{"name": "Noix", "quantity": 30, "unit": "g"},
{"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
{"name": "Tomates", "quantity": 100, "unit": "g"},
{"name": "Jeunes pousses", "quantity": 40, "unit": "g"},
{"name": "Pois chiches (en boite)", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
],
"name": "Salade fraîche", "steps": [
"Dans un plat: râpez les carottes.",
"Coupez les tomates en morceaux.",
"Epluchez les concombres et coupez les en dés grossiers.",
"Emiettez la feta.",
"Concassez les noix.",
"Préchauffez votre poêle.",
"Coupez le poulet en morceaux.",
"Quand la poêle est suffisament chaude, ajoutez les morceaux de poulet.",
"Quand le poulet est cuit, vous pouvez l'ajouter à votre salade."
"Ajouter les pois chiches et les jeunes pousses.",
"Dans un petit recipient mélangez l'huile d'olive et le vinaigre balsamique. Vous pouvez ajouter du citron.",
"Assaisonner avec le mélange. Vous pouvez ajouter des épices et du poivre selon vos envies.",
"Mélangez le tout avec une grosse cuillère."
], "type": ["lunch", "dinner"]},



            {"calories": 500,
             "proteins": 28,
             "carbohydrates": 66,
             "fats": 15,
             "ingredients": [
                 {"name": "Fromage blanc 0%", "quantity": 100, "unit": "g"},
                 {"name": "Mangue", "quantity": 50, "unit": "g"},
                 {"name": "Myrtilles", "quantity": 50, "unit": "g"},
                 {"name": "Framboises", "quantity": 50, "unit": "g"},
                 {"name": "Muesli (sans sucre ajouté)", "quantity": 65, "unit": "g"},
                 {"name": "Oeuf(s) entier(s)", "quantity": 2, "unit": "unit"},
             ],
             "name": "Fromage blanc fruité", "steps": [
                 "Dans un grand bol: versez le fromage blanc et ajoutez les myrtilles et les framboises.",
                 "Coupez la mangue en dés et ajoutez les morceaux au fromage blanc.",
                 "Ajoutez le muesli et mélangez.",
                 "Préparez les oeufs à part selon vos préférences, au plat, en omelette ou autre."
             ], "type": ["breakfast", "snack"]},
            
            {
                "calories": 500,
                "proteins": 42,
                "carbohydrates": 39,
                "fats": 19,
                "ingredients": [
                    {"name": "Oeuf(s) entier(s)", "quantity": 3, "unit": "unit"},
                    {"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
                    {"name": "Poivron", "quantity": 80, "unit": "g"},
                    {"name": "Champignons de Paris", "quantity": 80, "unit": "g"},
                    {"name": "Riz complet", "quantity": 50, "unit": "g"},
                ],
                "name": "Omelette", "steps": [
                    "Dans un grand recipient: fouettez le oeufs. Vous pouvez ajouter du poivre et des épices selon vos préferences.",
                    "Dans un plat, coupez le blanc de poulet et les poivrons en dés.",
                    "Versez dans une poêle chaude votre mélange d'oeufs fouettés.",
                    "Ajoutez-y le poulet et les poivrons.",
                    "Laissez cuire jusqu'à ce que l'omelette soit prête.",
                    "Pour la cuisson du riz, référez-vous aux instructions présentes sur l'emballage (typiquement environ 10min dans une casserole d'eau bouillante)."
                ], "type": ['lunch', 'dinner']
            },


            {"calories": 500,
             "proteins": 37,
             "carbohydrates": 23,
             "fats": 30,
             "ingredients": [
                 {"name": "Fromage blanc 0%", "quantity": 100, "unit": "g"},
                 {"name": "Beurre de cacahuètes", "quantity": 20, "unit": "g"},
                 {"name": "Myrtilles", "quantity": 30, "unit": "g"},
                 {"name": "Framboises", "quantity": 30, "unit": "g"},
                 {"name": "Pomme", "quantity": 30, "unit": "g"},
                 {"name": "Graines de courge", "quantity": 20, "unit": "g"},
                 {"name": "Flocons de soja", "quantity": 50, "unit": "g"},
             ],
             "name": "Fromage blanc fruité 2", "steps":[
                 "Dans un grand bol: versez le fromage blanc et le beurre de cacahuètes puis mélangez jusqu'à l'obtention d'un mélange homogène.",
                 "Ajoutez les myrtilles et les framboises.",
                 "Coupez la pomme en dés et ajoutez les morceaux au fromage blanc.",
                 "Ajoutez les flocons de soja et mélangez.",
                 "Ajoutez les graines de courge."
             ], "type": ["breakfast", "snack"]},
    


            {"calories": 500,
             "proteins": 28,
             "carbohydrates": 28,
             "fats": 30,
             "ingredients": [
                 {"name": "Carottes râpées", "quantity": 50, "unit": "g"},
                 {"name": "Concombre", "quantity": 50, "unit": "g"},
                 {"name": "Feta", "quantity": 15, "unit": "g"},
                 {"name": "Noix", "quantity": 20, "unit": "g"},
                 {"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
                 {"name": "Tomates", "quantity": 100, "unit": "g"},
                 {"name": "Jeunes pousses", "quantity": 40, "unit": "g"},
                 {"name": "Pois chiches (en boite)", "quantity": 60, "unit": "g"},
                 {"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
                 {"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
             ],
             "name": "Salade fraîche", "steps": [
                 "Dans un plat: râpez les carottes.",
                 "Coupez les tomates en morceaux.",
                 "Epluchez les concombres et coupez les en dés grossiers.",
                 "Emiettez la feta.",
                 "Concassez les noix.",
                 "Préchauffez votre poêle.",
                 "Coupez le poulet en morceaux.",
                 "Quand la poêle est suffisament chaude, ajoutez les morceaux de poulet.",
                 "Quand le poulet est cuit, vous pouvez l'ajouter à votre salade."
                 "Ajouter les pois chiches et les jeunes pousses.",
                 "Dans un petit recipient mélangez l'huile d'olive et le vinaigre balsamique. Vous pouvez ajouter du citron.",
                 "Assaisonner avec le mélange. Vous pouvez ajouter des épices et du poivre selon vos envies.",
                 "Mélangez le tout avec une grosse cuillère."
                 
             ], "type": ["lunch", "dinner"]},
            {"calories": 750,
"proteins": 46,
"carbohydrates": 106,
"fats": 16,
"ingredients": [
{"name": "Fromage blanc 0%", "quantity": 280, "unit": "g"},
{"name": "Mangue", "quantity": 70, "unit": "g"},
{"name": "Myrtilles", "quantity": 50, "unit": "g"},
{"name": "Banane", "quantity": 100, "unit": "g"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
{"name": "Muesli (sans sucre ajouté)", "quantity": 80, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 2, "unit": "unit"},
],
"name": "Fromage blanc fruité", "steps": [
"Dans un grand bol: versez le fromage blanc et ajoutez les myrtilles et les framboises.",
"Coupez la mangue en dés et ajoutez les morceaux au fromage blanc.",
"Coupez la banane en tranches et ajoutez les morceaux au fromage blanc.",
"Ajoutez le muesli et mélangez.",
"Préparez les oeufs à part selon vos préférences, au plat, en omelette ou autre."
], "type": ["breakfast", "snack"]},



{"calories": 750,
"proteins": 48,
"carbohydrates": 93,
"fats": 21,
"ingredients": [
{"name": "Oeuf(s) entier(s)", "quantity": 3, "unit": "unit"},
{"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
{"name": "Poivron", "quantity": 80, "unit": "g"},
{"name": "Champignons de Paris", "quantity": 80, "unit": "g"},
{"name": "Riz complet", "quantity": 125, "unit": "g"},
],
"name": "Omelette", "steps": [
"Dans un grand recipient: fouettez le oeufs. Vous pouvez ajouter du poivre et des épices selon vos préferences.",
"Dans un plat, coupez le blanc de poulet et les poivrons en dés.",
"Versez dans une poêle chaude votre mélange d'oeufs fouettés.",
"Ajoutez-y le poulet et les poivrons.",
"Laissez cuire jusqu'à ce que l'omelette soit prête.",
"Pour la cuisson du riz, référez-vous aux instructions présentes sur l'emballage (typiquement environ 10min dans une casserole d'eau bouillante)."
], "type": ['lunch', 'dinner']
},



{"calories": 750,
"proteins": 47,
"carbohydrates": 38,
"fats": 48,
"ingredients": [
{"name": "Fromage blanc 0%", "quantity": 100, "unit": "g"},
{"name": "Beurre de cacahuètes", "quantity": 50, "unit": "g"},
{"name": "Myrtilles", "quantity": 30, "unit": "g"},
{"name": "Framboises", "quantity": 30, "unit": "g"},
{"name": "Pomme", "quantity": 100, "unit": "g"},
{"name": "Graines de courge", "quantity": 20, "unit": "g"},
{"name": "Flocons de soja", "quantity": 60, "unit": "g"},
],
"name": "Fromage blanc fruité 2", "steps":[
"Dans un grand bol: versez le fromage blanc et le beurre de cacahuètes puis mélangez jusqu'à l'obtention d'un mélange homogène.",
"Ajoutez les myrtilles et les framboises.",
"Coupez la pomme en dés et ajoutez les morceaux au fromage blanc.",
"Ajoutez les flocons de soja et mélangez.",
"Ajoutez les graines de courge."
], "type": ["breakfast", "snack"]},


{"calories": 750,
"proteins": 41,
"carbohydrates": 47,
"fats": 43,
"ingredients": [
{"name": "Carottes râpées", "quantity": 50, "unit": "g"},
{"name": "Concombre", "quantity": 50, "unit": "g"},
{"name": "Feta", "quantity": 20, "unit": "g"},
{"name": "Noix", "quantity": 40, "unit": "g"},
{"name": "Blanc de poulet", "quantity": 100, "unit": "g"},
{"name": "Tomates", "quantity": 100, "unit": "g"},
{"name": "Jeunes pousses", "quantity": 40, "unit": "g"},
{"name": "Pois chiches (en boite)", "quantity": 150, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
],
"name": "Salade fraîche", "steps": [
"Dans un plat: râpez les carottes.",
"Coupez les tomates en morceaux.",
"Epluchez les concombres et coupez les en dés grossiers.",
"Emiettez la feta.",
"Concassez les noix.",
"Préchauffez votre poêle.",
"Coupez le poulet en morceaux.",
"Quand la poêle est suffisament chaude, ajoutez les morceaux de poulet.",
"Quand le poulet est cuit, vous pouvez l'ajouter à votre salade."
"Ajouter les pois chiches et les jeunes pousses.",
"Dans un petit recipient mélangez l'huile d'olive et le vinaigre balsamique. Vous pouvez ajouter du citron.",
"Assaisonner avec le mélange. Vous pouvez ajouter des épices et du poivre selon vos envies.",
"Mélangez le tout avec une grosse cuillère."
], "type": ["lunch", "dinner"]},

            {"calories": 400,
"proteins": 24,
"carbohydrates": 58,
"fats": 8,
"ingredients": [
{"name": "Fromage blanc 0%", "quantity": 150, "unit": "g"},
{"name": "Mangue", "quantity": 30, "unit": "g"},
{"name": "Myrtilles", "quantity": 50, "unit": "g"},
{"name": "Banane", "quantity": 50, "unit": "g"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
{"name": "Muesli (sans sucre ajouté)", "quantity": 40, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 1, "unit": "unit"},
],
"name": "Fromage blanc fruité", "steps": [
"Dans un grand bol: versez le fromage blanc et ajoutez les myrtilles et les framboises.",
"Coupez la mangue en dés et ajoutez les morceaux au fromage blanc.",
"Coupez la banane en tranches et ajoutez les morceaux au fromage blanc.",
"Ajoutez le muesli et mélangez.",
"Préparez les oeufs à part selon vos préférences, au plat, en omelette ou autre."
], "type": ["breakfast", "snack"]},


{"calories": 400,
"proteins": 34,
"carbohydrates": 25,
"fats": 19,
"ingredients": [
{"name": "Oeuf(s) entier(s)", "quantity": 3, "unit": "unit"},
{"name": "Blanc de poulet", "quantity": 50, "unit": "g"},
{"name": "Poivron", "quantity": 80, "unit": "g"},
{"name": "Champignons de Paris", "quantity": 80, "unit": "g"},
{"name": "Riz complet", "quantity": 30, "unit": "g"},
],
"name": "Omelette", "steps": [
"Dans un grand recipient: fouettez le oeufs. Vous pouvez ajouter du poivre et des épices selon vos préferences.",
"Dans un plat, coupez le blanc de poulet et les poivrons en dés.",
"Versez dans une poêle chaude votre mélange d'oeufs fouettés.",
"Ajoutez-y le poulet et les poivrons.",
"Laissez cuire jusqu'à ce que l'omelette soit prête.",
"Pour la cuisson du riz, référez-vous aux instructions présentes sur l'emballage (typiquement environ 10min dans une casserole d'eau bouillante)."
], "type": ['lunch', 'dinner']
},



{"calories": 300,
"proteins": 18,
"carbohydrates": 18,
"fats": 19,
"ingredients": [
{"name": "Fromage blanc 0%", "quantity": 100, "unit": "g"},
{"name": "Beurre de cacahuètes", "quantity": 20, "unit": "g"},
{"name": "Myrtilles", "quantity": 30, "unit": "g"},
{"name": "Framboises", "quantity": 30, "unit": "g"},
{"name": "Graines de courge", "quantity": 20, "unit": "g"},
],
"name": "Fromage blanc fruité 2", "steps":[
"Dans un grand bol: versez le fromage blanc et le beurre de cacahuètes puis mélangez jusqu'à l'obtention d'un mélange homogène.",
"Ajoutez les myrtilles et les framboises.",
"Ajoutez les graines de courge."
], "type": ["breakfast", "snack"]},



{"calories": 400,
"proteins": 25,
"carbohydrates": 26,
"fats": 21,
"ingredients": [
{"name": "Carottes râpées", "quantity": 70, "unit": "g"},
{"name": "Concombre", "quantity": 50, "unit": "g"},
{"name": "Feta", "quantity": 15, "unit": "g"},
{"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
{"name": "Tomates", "quantity": 100, "unit": "g"},
{"name": "Jeunes pousses", "quantity": 40, "unit": "g"},
{"name": "Pois chiches (en boite)", "quantity": 70, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
],
"name": "Salade fraîche", "steps": [
"Dans un plat: râpez les carottes.",
"Coupez les tomates en morceaux.",
"Epluchez les concombres et coupez les en dés grossiers.",
"Emiettez la feta.",
"Préchauffez votre poêle.",
"Coupez le poulet en morceaux.",
"Quand la poêle est suffisament chaude, ajoutez les morceaux de poulet.",
"Quand le poulet est cuit, vous pouvez l'ajouter à votre salade."
"Ajouter les pois chiches et les jeunes pousses.",
"Dans un petit recipient mélangez l'huile d'olive et le vinaigre balsamique. Vous pouvez ajouter du citron.",
"Assaisonner avec le mélange. Vous pouvez ajouter des épices et du poivre selon vos envies.",
"Mélangez le tout avec une grosse cuillère."
], "type": ["lunch", "dinner"]},

{"calories": 400,
"proteins": 24,
"carbohydrates": 58,
"fats": 8,
"ingredients": [
{"name": "Fromage blanc 0%", "quantity": 150, "unit": "g"},
{"name": "Mangue", "quantity": 30, "unit": "g"},
{"name": "Myrtilles", "quantity": 50, "unit": "g"},
{"name": "Banane", "quantity": 50, "unit": "g"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
{"name": "Muesli (sans sucre ajouté)", "quantity": 40, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 1, "unit": "unit"},
],             
"name": "Fromage blanc fruité", "steps": [
"Dans un grand bol: versez le fromage blanc et ajoutez les myrtilles et les framboises.",
"Coupez la mangue en dés et ajoutez les morceaux au fromage blanc.",
"Coupez la banane en tranches et ajoutez les morceaux au fromage blanc.",
"Ajoutez le muesli et mélangez.",
"Préparez les oeufs à part selon vos préférences, au plat, en omelette ou autre."
], "type": ["breakfast", "snack"]},



{"calories": 450,
"proteins": 41,
"carbohydrates": 29,
"fats": 19,
"ingredients": [
{"name": "Oeuf(s) entier(s)", "quantity": 3, "unit": "unit"},
{"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
{"name": "Poivron", "quantity": 80, "unit": "g"},
{"name": "Champignons de Paris", "quantity": 80, "unit": "g"},
{"name": "Riz complet", "quantity": 35, "unit": "g"},
],
"name": "Omelette", "steps": [
"Dans un grand recipient: fouettez le oeufs. Vous pouvez ajouter du poivre et des épices selon vos préferences.",
"Dans un plat, coupez le blanc de poulet et les poivrons en dés.",
"Versez dans une poêle chaude votre mélange d'oeufs fouettés.",
"Ajoutez-y le poulet et les poivrons.",
"Laissez cuire jusqu'à ce que l'omelette soit prête.",
"Pour la cuisson du riz, référez-vous aux instructions présentes sur l'emballage (typiquement environ 10min dans une casserole d'eau bouillante)."
], "type": ['lunch', 'dinner']
},


{"calories": 500,
"proteins": 37,
"carbohydrates": 23,
"fats": 30,
"ingredients": [
{"name": "Fromage blanc 0%", "quantity": 100, "unit": "g"},
{"name": "Beurre de cacahuètes", "quantity": 20, "unit": "g"},
{"name": "Myrtilles", "quantity": 30, "unit": "g"},
{"name": "Framboises", "quantity": 30, "unit": "g"},
{"name": "Pomme", "quantity": 30, "unit": "g"},
{"name": "Graines de courge", "quantity": 20, "unit": "g"},
{"name": "Flocons de soja", "quantity": 50, "unit": "g"},
],
"name": "Fromage blanc fruité 2", "steps":[
"Dans un grand bol: versez le fromage blanc et le beurre de cacahuètes puis mélangez jusqu'à l'obtention d'un mélange homogène.",
"Ajoutez les myrtilles et les framboises.",
"Coupez la pomme en dés et ajoutez les morceaux au fromage blanc.",
"Ajoutez les flocons de soja et mélangez.",
"Ajoutez les graines de courge."
], "type": ["breakfast", "snack"]},



{"calories": 450,
"proteins": 26,
"carbohydrates": 27,
"fats": 25,
"ingredients": [
{"name": "Carottes râpées", "quantity": 70, "unit": "g"},
{"name": "Concombre", "quantity": 50, "unit": "g"},
{"name": "Feta", "quantity": 15, "unit": "g"},
{"name": "Noix", "quantity": 10, "unit": "g"},
{"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
{"name": "Tomates", "quantity": 100, "unit": "g"},
{"name": "Jeunes pousses", "quantity": 40, "unit": "g"},
{"name": "Pois chiches (en boite)", "quantity": 60, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
],
"name": "Salade fraîche", "steps": [
"Dans un plat: râpez les carottes.",
"Coupez les tomates en morceaux.",
"Epluchez les concombres et coupez les en dés grossiers.",
"Emiettez la feta.",
"Concassez les noix.",
"Préchauffez votre poêle.",
"Coupez le poulet en morceaux.",
"Quand la poêle est suffisament chaude, ajoutez les morceaux de poulet.",
"Quand le poulet est cuit, vous pouvez l'ajouter à votre salade."
"Ajouter les pois chiches et les jeunes pousses.",
"Dans un petit recipient mélangez l'huile d'olive et le vinaigre balsamique. Vous pouvez ajouter du citron.",
"Assaisonner avec le mélange. Vous pouvez ajouter des épices et du poivre selon vos envies.",
"Mélangez le tout avec une grosse cuillère."
], "type": ["lunch", "dinner"]},

{"calories": 300,
"proteins": 17,
"carbohydrates": 26,
"fats": 13,
"ingredients": [
{"name": "Flocons d'avoine", "quantity": 30, "unit": "g"},
{"name": "Lait de riz", "quantity": 40, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 2, "unit": "unit"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 350,
"proteins": 19,
"carbohydrates": 37,
"fats": 15,
"ingredients": [
{"name": "Flocons d'avoine", "quantity": 45, "unit": "g"},
{"name": "Lait de riz", "quantity": 50, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 2, "unit": "unit"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 400,
"proteins": 24,
"carbohydrates": 33,
"fats": 20,
"ingredients": [
{"name": "Flocons d'avoine", "quantity": 40, "unit": "g"},
{"name": "Lait de riz", "quantity": 40, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 3, "unit": "unit"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 500,
"proteins": 28,
"carbohydrates": 36,
"fats": 28,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 15, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 40, "unit": "g"},
{"name": "Lait de riz", "quantity": 40, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 3, "unit": "unit"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 550,
"proteins": 30,
"carbohydrates": 40,
"fats": 30,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 20, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 45, "unit": "g"},
{"name": "Lait de riz", "quantity": 40, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 3, "unit": "unit"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 600,
"proteins": 35,
"carbohydrates": 37,
"fats": 36,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 20, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 40, "unit": "g"},
{"name": "Lait de riz", "quantity": 40, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 4, "unit": "unit"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 650,
"proteins": 37,
"carbohydrates": 45,
"fats": 37,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 20, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 50, "unit": "g"},
{"name": "Lait de riz", "quantity": 50, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 4, "unit": "unit"},
{"name": "Framboises", "quantity": 60, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 700,
"proteins": 39,
"carbohydrates": 50,
"fats": 40,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 25, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 55, "unit": "g"},
{"name": "Lait de riz", "quantity": 60, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 4, "unit": "g"},
{"name": "Framboises", "quantity": 60, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 750,
"proteins": 40,
"carbohydrates": 54,
"fats": 43,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 30, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 60, "unit": "g"},
{"name": "Lait de riz", "quantity": 60, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 4, "unit": "unit"},
{"name": "Framboises", "quantity": 60, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 800,
"proteins": 42,
"carbohydrates": 63,
"fats": 43,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 30, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 70, "unit": "g"},
{"name": "Lait de riz", "quantity": 80, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 4, "unit": "unit"},
{"name": "Framboises", "quantity": 60, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 850,
"proteins": 44,
"carbohydrates": 65,
"fats": 49,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 40, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 70, "unit": "g"},
{"name": "Lait de riz", "quantity": 80, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 4, "unit": "unit"},
{"name": "Framboises", "quantity": 60, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 900,
"proteins": 46,
"carbohydrates": 74,
"fats": 50,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 40, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 85, "unit": "g"},
{"name": "Lait de riz", "quantity": 80, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 4, "unit": "unit"},
{"name": "Framboises", "quantity": 60, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 950,
"proteins": 48,
"carbohydrates": 84,
"fats": 51,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 40, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 100, "unit": "g"},
{"name": "Lait de riz", "quantity": 80, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 4, "unit": "unit"},
{"name": "Framboises", "quantity": 60, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 1000,
"proteins": 50,
"carbohydrates": 86,
"fats": 56,
"ingredients": [
{"name": "Beurre de cacahuètes", "quantity": 50, "unit": "g"},
{"name": "Flocons d'avoine", "quantity": 100, "unit": "g"},
{"name": "Lait de riz", "quantity": 80, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 4, "unit": "unit"},
{"name": "Framboises", "quantity": 60, "unit": "g"},
],
"name": "Flocons d'avoine et Omelette", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},




{"calories": 300,
"proteins": 21,
"carbohydrates": 11,
"fats": 18,
"ingredients": [
{"name": "Filet de poulet", "quantity": 80, "unit": "g"},
{"name": "Tomates", "quantity": 100, "unit": "g"},
{"name": "Concombre", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 350,
"proteins": 23,
"carbohydrates": 13,
"fats": 23,
"ingredients": [
{"name": "Filet de poulet", "quantity": 80, "unit": "g"},
{"name": "Tomates", "quantity": 100, "unit": "g"},
{"name": "Concombre", "quantity": 100, "unit": "g"},
{"name": "Noix", "quantity": 10, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 400,
"proteins": 24,
"carbohydrates": 17,
"fats": 26,
"ingredients": [
{"name": "Filet de poulet", "quantity": 80, "unit": "g"},
{"name": "Tomates", "quantity": 150, "unit": "g"},
{"name": "Concombre", "quantity": 100, "unit": "g"},
{"name": "Noix", "quantity": 15, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 450,
"proteins": 27,
"carbohydrates": 25,
"fats": 26,
"ingredients": [
{"name": "Pois chiches (en boite)", "quantity": 50, "unit": "g"},
{"name": "Filet de poulet", "quantity": 80, "unit": "g"},
{"name": "Tomates", "quantity": 150, "unit": "g"},
{"name": "Concombre", "quantity": 100, "unit": "g"},
{"name": "Noix", "quantity": 15, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 500,
"proteins": 34,
"carbohydrates": 29,
"fats": 27,
"ingredients": [
{"name": "Pois chiches (en boite)", "quantity": 70, "unit": "g"},
{"name": "Filet de poulet", "quantity": 100, "unit": "g"},
{"name": "Tomates", "quantity": 150, "unit": "g"},
{"name": "Concombre", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 15, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 550,
"proteins": 35,
"carbohydrates": 31,
"fats": 30,
"ingredients": [
{"name": "Pois chiches (en boite)", "quantity": 80, "unit": "g"},
{"name": "Filet de poulet", "quantity": 100, "unit": "g"},
{"name": "Tomates", "quantity": 150, "unit": "g"},
{"name": "Concombre", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 20, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 600,
"proteins": 38,
"carbohydrates": 36,
"fats": 32,
"ingredients": [
{"name": "Pois chiches (en boite)", "quantity": 100, "unit": "g"},
{"name": "Filet de poulet", "quantity": 100, "unit": "g"},
{"name": "Tomates", "quantity": 150, "unit": "g"},
{"name": "Concombre", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 25, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 750,
"proteins": 38,
"carbohydrates": 40,
"fats": 47,
"ingredients": [
{"name": "Pois chiches (en boite)", "quantity": 100, "unit": "g"},
{"name": "Filet de poulet", "quantity": 100, "unit": "g"},
{"name": "Tomates", "quantity": 150, "unit": "g"},
{"name": "Concombre", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 25, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 2, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 800,
"proteins": 44,
"carbohydrates": 43,
"fats": 48,
"ingredients": [
{"name": "Pois chiches (en boite)", "quantity": 120, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Tomates", "quantity": 150, "unit": "g"},
{"name": "Concombre", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 25, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 2, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 850,
"proteins": 47,
"carbohydrates": 49,
"fats": 51,
"ingredients": [
{"name": "Pois chiches (en boite)", "quantity": 150, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Tomates", "quantity": 150, "unit": "g"},
{"name": "Concombre", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 30, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 2, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 900,
"proteins": 54,
"carbohydrates": 51,
"fats": 52,
"ingredients": [
{"name": "Pois chiches (en boite)", "quantity": 160, "unit": "g"},
{"name": "Filet de poulet", "quantity": 150, "unit": "g"},
{"name": "Tomates", "quantity": 150, "unit": "g"},
{"name": "Concombre", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 30, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 2, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "<RECIPE_NAME>", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},






{"calories": 300,
"proteins": 20,
"carbohydrates": 7,
"fats": 22,
"ingredients": [
{"name": "Thon au naturel", "quantity": 60, "unit": "g"},
{"name": "Graines de courge", "quantity": 10, "unit": "g"},
{"name": "Poivron", "quantity": 50, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 350,
"proteins": 28,
"carbohydrates": 8,
"fats": 22,
"ingredients": [
{"name": "Thon au naturel", "quantity": 90, "unit": "g"},
{"name": "Graines de courge", "quantity": 10, "unit": "g"},
{"name": "Poivron", "quantity": 50, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 400,
"proteins": 31,
"carbohydrates": 8,
"fats": 27,
"ingredients": [
{"name": "Thon au naturel", "quantity": 90, "unit": "g"},
{"name": "Graines de courge", "quantity": 10, "unit": "g"},
{"name": "Poivron", "quantity": 50, "unit": "g"},
{"name": "Graines de lin", "quantity": 15, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 450,
"proteins": 33,
"carbohydrates": 11,
"fats": 29,
"ingredients": [
{"name": "Thon au naturel", "quantity": 90, "unit": "g"},
{"name": "Graines de courge", "quantity": 15, "unit": "g"},
{"name": "Poivron", "quantity": 100, "unit": "g"},
{"name": "Graines de lin", "quantity": 15, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 500,
"proteins": 36,
"carbohydrates": 12,
"fats": 33,
"ingredients": [
{"name": "Thon au naturel", "quantity": 90, "unit": "g"},
{"name": "Graines de courge", "quantity": 20, "unit": "g"},
{"name": "Poivron", "quantity": 100, "unit": "g"},
{"name": "Graines de lin", "quantity": 20, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 550,
"proteins": 38,
"carbohydrates": 13,
"fats": 37,
"ingredients": [
{"name": "Thon au naturel", "quantity": 90, "unit": "g"},
{"name": "Graines de courge", "quantity": 25, "unit": "g"},
{"name": "Poivron", "quantity": 100, "unit": "g"},
{"name": "Graines de lin", "quantity": 25, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 600,
"proteins": 33,
"carbohydrates": 15,
"fats": 44,
"ingredients": [
{"name": "Thon au naturel", "quantity": 90, "unit": "g"},
{"name": "Graines de courge", "quantity": 15, "unit": "g"},
{"name": "Poivron", "quantity": 100, "unit": "g"},
{"name": "Graines de lin", "quantity": 15, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 2, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 650,
"proteins": 36,
"carbohydrates": 16,
"fats": 48,
"ingredients": [
{"name": "Thon au naturel", "quantity": 90, "unit": "g"},
{"name": "Graines de courge", "quantity": 20, "unit": "g"},
{"name": "Poivron", "quantity": 100, "unit": "g"},
{"name": "Graines de lin", "quantity": 20, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 2, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 700,
"proteins": 38,
"carbohydrates": 17,
"fats": 52,
"ingredients": [
{"name": "Thon au naturel", "quantity": 90, "unit": "g"},
{"name": "Graines de courge", "quantity": 25, "unit": "g"},
{"name": "Poivron", "quantity": 100, "unit": "g"},
{"name": "Graines de lin", "quantity": 25, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 2, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 750,
"proteins": 48,
"carbohydrates": 17,
"fats": 55,
"ingredients": [
{"name": "Thon au naturel", "quantity": 120, "unit": "g"},
{"name": "Graines de courge", "quantity": 30, "unit": "g"},
{"name": "Poivron", "quantity": 100, "unit": "g"},
{"name": "Graines de lin", "quantity": 25, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 2, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 800,
"proteins": 50,
"carbohydrates": 18,
"fats": 59,
"ingredients": [
{"name": "Thon au naturel", "quantity": 120, "unit": "g"},
{"name": "Graines de courge", "quantity": 35, "unit": "g"},
{"name": "Poivron", "quantity": 100, "unit": "g"},
{"name": "Graines de lin", "quantity": 30, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 2, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Salade de thon", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},




{"calories": 300,
"proteins": 27,
"carbohydrates": 10,
"fats": 18,
"ingredients": [
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 350,
"proteins": 32,
"carbohydrates": 20,
"fats": 18,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 20, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
 "name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 400,
"proteins": 34,
"carbohydrates": 25,
"fats": 18,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 30, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "g"},
{"name": "Moutarde", "quantity": 1, "unit": "g"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 450,
"proteins": 36,
"carbohydrates": 28,
"fats": 23,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 30, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 10, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 500,
"proteins": 38,
"carbohydrates": 33,
"fats": 23,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 40, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 10, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 550,
"proteins": 40,
"carbohydrates": 35,
"fats": 28,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 40, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 20, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 600,
"proteins": 44,
"carbohydrates": 43,
"fats": 28,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 55, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 20, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 650,
"proteins": 46,
"carbohydrates": 46,
"fats": 31,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 60, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 25, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 700,
"proteins": 51,
"carbohydrates": 57,
"fats": 31,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 80, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 25, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 750,
"proteins": 45,
"carbohydrates": 45,
"fats": 43,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 60, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 20, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


{"calories": 800,
"proteins": 48,
"carbohydrates": 52,
"fats": 46,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 70, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 25, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},



{"calories": 850,
"proteins": 51,
"carbohydrates": 57,
"fats": 46,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 80, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 25, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},



{"calories": 900,
"proteins": 56,
"carbohydrates": 67,
"fats": 46,
"ingredients": [
{"name": "Lentilles vertes", "quantity": 100, "unit": "g"},
{"name": "Filet de poulet", "quantity": 120, "unit": "g"},
{"name": "Noix", "quantity": 25, "unit": "g"},
{"name": "Endives", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 2, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
{"name": "Moutarde", "quantity": 1, "unit": "càs"},
],
"name": "Poulet lentilles", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},



{"calories": 750,
"proteins": 32,
"carbohydrates": 81,
"fats": 36,
"ingredients": [
{"name": "Farine de sarrasin", "quantity": 100, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 3, "unit": "unit"},
{"name": "Lait de riz", "quantity": 100, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
],
"name": "Panckakes", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},

{"calories": 500,
"proteins": 61,
"carbohydrates": 57,
"fats": 2,
"ingredients": [
{"name": "Banane", "quantity": 270, "unit": "g"},
{"name": "Gold Standard Whey", "quantity": 70, "unit": "g"},
],
 "name": "Whey et banane", "steps": ["<RECIPE_STEPS>"], "type": "<RECIPE_TYPE>"},


        ]




        
    def get_recipe(self, name, calories):
        try:
            calories = int(calories)
        except ValueError:
            return None
        
        recipe = list(
                filter(
                    lambda x: name == x['name']
                    and x['calories'] == calories,
                    self.recipes
                )
        )
        if recipe and len(recipe) > 0:
            return recipe[0]
        
        return None
