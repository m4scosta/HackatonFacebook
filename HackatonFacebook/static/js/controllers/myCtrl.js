/**
 * Created by bustamante on 5/15/15.
 */

angular.module('MyApp').controller('MyCtrl', function(Ajax, $scope){
    $scope.getByAjax = function(){
        Ajax.get('get/teste').success(function(result,a, b, c){
            $scope.ajax_msg = result.ajax_msg;
        });
    }
});
