<script>
  import * as echarts from 'echarts';   // importa la librería de gráficos
  import { onMount } from 'svelte';     // importa el ciclo de vida onMount

  let pieChartEl;   // variable para almacenar la referencia al <div> donde se dibujará el gráfico circular
  let barChartEl;   // variable para almacenar la referencia al <div> donde se dibujará el gráfico de barras

  onMount(async () => {
    // Petición al backend
    const res = await fetch("/data");
    const data = await res.json();   // Convertimos la respuesta en un objeto JS

    // Inicializa el gráfico circular
    const pie = echarts.init(pieChartEl);
    pie.setOption({
      title: { text: 'Productos', left: 'center' },
      tooltip: { trigger: 'item' },
      series: [{
        name: 'Productos',
        type: 'pie',
        radius: '50%',
        data: data.piechart.labels.map((label, i) => ({
          value: data.piechart.values[i],
          name: label
        }))
      }]
    });

    // Inicializa el gráfico de barras
    const bar = echarts.init(barChartEl);
    bar.setOption({
      title: { text: 'Ventas por Mes', left: 'center' },
      tooltip: {},
      xAxis: {
        type: 'category',
        data: data.barplot.categories
      },
      yAxis: { type: 'value' },
      series: [{
        type: 'bar',
        data: data.barplot.values
      }]
    });
  });
</script>

<!-- Estilos para los gráficos -->
<style>
  .chart {
    width: 100%;
    max-width: 600px;
    height: 400px;
    margin: auto;
    margin-top: 2rem;
  }
</style>

<h1 style="text-align: center;">Dashboard de Datos</h1>
<div bind:this={pieChartEl} class="chart"></div>
<div bind:this={barChartEl} class="chart"></div>
