/**
 * Created by PerminovMA@live.ru on 01.08.15.
 */


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