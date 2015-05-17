/**
 * Created by bustamante on 3/5/15.
 */
angular.module('HackathonApp', ['ajax', 'ui.utils']);

angular.module('HackathonApp').config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
});
