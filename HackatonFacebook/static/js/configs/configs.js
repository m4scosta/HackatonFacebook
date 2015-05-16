/**
 * Created by bustamante on 3/5/15.
 */
angular.module('MyApp', ['ui.bootstrap', 'ajax']);

angular.module('MyApp').config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
});
