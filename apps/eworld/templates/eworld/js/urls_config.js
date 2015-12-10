/**
 * Created by PerminovMA@live.ru on 13.07.15.
 */

// URLs config
app.constant("URLs", {
        authorization: "{% url 'profile:authorization' %}",
        auctions_data_url: "{% url 'eworld:rest_api_urls:auctions_data-list' %}",
        orders_data_url: "{% url 'eworld:rest_api_urls:orders_data-list' %}",
        categories_data_url: "{% url 'eworld:rest_api_urls:categories_data-list' %}",
    });