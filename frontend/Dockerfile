FROM gitlab.ldv.ei.tum.de:5005/cellphaser/cp-containers/cp-component-frontend-template:latest
# To have a look at what's available in this image already have a look at:
# https://gitlab.ldv.ei.tum.de/cellphaser/cp-containers/-/tree/master/cp-component-frontend-template

# install additional packages here
#RUN yarn add <somepackage>
RUN yarn add chart.js vue-chartjs vue-chart-3 jquery apexcharts vue3-apexcharts vega-embed vega vega-lite vue-vega echarts v-charts vue-echarts plotly.js-dist-min
COPY . .
