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
        return $resource(URLs.auctions_data_url, {});
    }
]);

app.factory('CategoriesService', [
    '$resource', 'URLs', function($resource, URLs) {
        return $resource(URLs.categories_data_url, {});
    }
]);

app.factory('BetsService', [
    '$resource', 'URLs', function($resource, URLs) {
        return $resource(URLs.bets_data_url, {});
    }
]);