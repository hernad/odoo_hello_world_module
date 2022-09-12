odoo.define('hello_world.main', function (require) {  
    const AbstractAction = require('web.AbstractAction');  
    const core = require('web.core');  
    
    //const OurAction = AbstractAction.extend({
    //          start: function () {          
    //            this.$el.html('hello');      
    //          }  
    //       });
    const OurAction = AbstractAction.extend({  
        template: "hello_world.helloTemplate",  
        info: "component info: Ernad Husremović"
    });

    core.action_registry.add('hello_world.action', OurAction);}
);                    