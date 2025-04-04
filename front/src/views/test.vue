<template>
    <div>
      <h1>Графики</h1>
      <div style="width: 400px; margin: 0 auto;">
        <canvas id="pieChart"></canvas>
      </div>
      <div style="width: 600px; margin: 0 auto;">
        <canvas id="barChart"></canvas>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { Chart, registerables } from 'chart.js';
  Chart.register(...registerables);
  
  const pieChart = ref(null);
  const barChart = ref(null);
  
  onMounted(() => {
    createPieChart();
    createBarChart();
  });
  
  const createPieChart = () => {
    const ctx = document.getElementById('pieChart').getContext('2d');
    pieChart.value = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Позитив', 'Негатив'],
        datasets: [{
          data: [70, 30], // Пример данных, замени на свои
          backgroundColor: [
            'rgba(75, 192, 192, 0.7)', // Цвет для позитивной части
            'rgba(255, 99, 132, 0.7)'  // Цвет для негативной части
          ],
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      }
    });
  };
  
  const createBarChart = () => {
    const ctx = document.getElementById('barChart').getContext('2d');
    barChart.value = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Отправленные', 'Полученные'],
        datasets: [
          {
            label: 'Лайки',
            data: [40, 60], // Пример данных, замени на свои
            backgroundColor: 'rgba(75, 192, 192, 0.7)', // Зеленый
            borderWidth: 1
          },
          {
            label: 'Дизлайки',
            data: [20, 10], // Пример данных, замени на свои
            backgroundColor: 'rgba(255, 99, 132, 0.7)', // Красный
            borderWidth: 1
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            stacked: true
          },
          y: {
            stacked: true
          }
        }
      }
    });
  };
  </script>
  
  <style scoped>
  
  </style>
  