const f=require('node:fs');f.mkdirSync('jeu',{recursive:true});for(let p of ['index.html','style.css','app.js','engine.mjs','content','assets'])f.cpSync(p,'jeu/'+p,{recursive:true});
