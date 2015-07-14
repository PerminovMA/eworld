/**
 * Created by PerminovMA@live.ru on 26.06.15.
 */

var app = angular.module('eworld_base_module', ['ui.bootstrap']);

app.config(function ($interpolateProvider, $httpProvider) {
    // allow django templates and angular to co-exist
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
});

app.controller("IndexPageController",
    function ($scope, $modal) {
        $scope.open_auth_modal = function () {
            var modalInstance = $modal.open({
                // animation: $scope.animationsEnabled,
                templateUrl: 'profile/authorization',
                controller: 'AuthorizationController'
                // size: size
            });
        }
    }
);


app.controller(
    "AuthorizationController",
    function ($scope, $http, $modalInstance, URLs) {
        //$scope.namee = items;

        $scope.testFunction = function () {
            alert(URLs.authorization);
        }

        $scope.submit = function () {
            $http({method: "POST", url: URLs.authorization, params: {email: $scope.email, password: $scope.password}}).
                success(function (data, status) {
                    $scope.status = status;
                    $scope.data = data;
                    console.log("SUCCESS");
                    console.log(status);
                    console.log(data);
                }).
                error(function (data, status) {
                    $scope.data = data || "Request failed";
                    $scope.status = status;
                    console.log("ERROR");
                    console.log(status + " " + data);

                });
        };

        $scope.cancel = function () {
            $modalInstance.dismiss('cancel');
        };
    });