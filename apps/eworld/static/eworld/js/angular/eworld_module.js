/**
 * Created by PerminovMA@live.ru on 26.06.15.
 */

var app = angular.module('eworld_base_module', ['ui.bootstrap', 'ngResource']);

app.config(function ($interpolateProvider, $httpProvider) {
    // allow django templates and angular to co-exist
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    // for meeting the django POST requests security requirements
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
});

app.controller("IndexPageController",
    function ($scope, $modal, URLs) {
        $scope.open_auth_modal = function () {
            var modalInstance = $modal.open({
                templateUrl: URLs.authorization,
                controller: 'AuthorizationController'
            });
        }
    }
);

app.controller(
    "AuthorizationController",
    function ($scope, $http, $modalInstance, URLs) {
        $scope.form_errors = [];
        $scope.submit = function () {
            $scope.form_errors = [];
            $http({method: "POST", url: URLs.authorization, data: {email: $scope.email, password: $scope.password}}).
                success(function (data, status) {
                    if (data.result === 'nok') {
                        for (var error_field_name in data.errors) {
                            $scope[error_field_name + "_error_status"] = data.errors[error_field_name][0];
                            $scope.form_errors.push(data.errors[error_field_name][0]);
                        }
                    } else if (data.result == 'ok') {
                        window.location.replace(data.redirect_url);
                    }
                }).
                error(function (data, status) {
                    alert("Произошла ошибка. Обратитесь к администратору. Status: " + status);
                });
        };

        $scope.cancel = function () {
            $modalInstance.dismiss('cancel');
        };
    });