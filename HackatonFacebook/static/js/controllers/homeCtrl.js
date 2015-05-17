/**
 * Created by bustamante on 5/16/15.
 */


    //window.myVar = {prop: "value1"};
    //var myVarWatch = (function() {
    //    var watches = {};
    //
    //    return {
    //        watch: function(callback) {
    //            var id = Math.random().toString();
    //            watches[id] = callback;
    //
    //            // Return a function that removes the listener
    //            return function() {
    //                watches[id] = null;
    //                delete watches[id];
    //            }
    //        },
    //        trigger: function() {
    //            for (var k in watches) {
    //                watches[k](window.myVar);
    //            }
    //        }
    //    }
    //})();
    //
    //setTimeout(function() {
    //    window.myVar.prop = "new value";
    //    myVarWatch.trigger();
    //}, 1000);

angular.module('HackathonApp').controller("homeCtrl", function($scope, $window){
    $scope.ingredients = [];
    $scope.recipes = [];
    $scope.small = false;
    $scope.viewproduct = false;
    $scope.openproduct = {};

    //var unbind = myVarWatch.watch(function(newVal) {
    //    console.log("the value changed!", newVal);
    //});
    //
    //// Unbind the listener when the scope is destroyed
    //$scope.$on('$destroy', unbind);

    //$scope.$watch(
    //    function () {
    //        return $window.test
    //    }, function(n,o){
    //        console.log("changed ",n);
    //    }
    //);
});

