/**
 * Created by bustamante on 3/5/15.
 */

window.has_attr = function(key, value, list){
    for(var i = 0; i < list.length; ++i){
        if(value == list[i][key])
            return true;
    }
    return false;
};

angular.module('HackathonApp', ['ajax', 'ui.utils']);

angular.module('HackathonApp').config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
});
