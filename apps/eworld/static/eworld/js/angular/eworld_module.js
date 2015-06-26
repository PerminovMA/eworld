/**
 * Created by PerminovMA@live.ru on 26.06.15.
 */

var app = angular.module('eworld_base_module', []);

app.config(function ($interpolateProvider) {
    //allow django templates and angular to co-exist
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

// URLs config
//app.constant("urls", {edit_campaign_url: "/control_panel/edit_campaign/"});