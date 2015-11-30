/**
 * Created by PerminovMA@live.ru on 01.08.15.
 */

app.factory('OrdersService', [
    '$resource', 'URLs', function($resource, URLs) {
        return $resource(URLs.orders_data_url, {});
    }
]);

app.factory('AuctionsService', [
    '$resource', 'URLs', function($resource, URLs) {
        return $resource(URLs.auctions_data_url, {}, {get_best_bets: {method:'GET', params:{},
            url:URLs.auctions_data_url+'best_bets', isArray:true}});
    }
]);

app.factory('CategoriesService', [
    '$resource', 'URLs', function($resource, URLs) {
        return $resource(URLs.categories_data_url, {});
    }
]);
