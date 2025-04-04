<script setup>
import location from "@/svg/location.vue";
import FooterNav from "@/components/FooterNav.vue";

import heart from "@/svg/heart.vue";
import dislike from "@/svg/dislike.vue";

import { ref, onMounted } from "vue";
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

const pieChart = ref(null);
const barChart = ref(null);

onMounted(() => {
  createPieChart();
  createBarChart();
});

const createPieChart = () => {
  const ctx = document.getElementById("pieChart").getContext("2d");
  pieChart.value = new Chart(ctx, {
    type: "pie",
    data: {
      labels: ["Лайки", "Дизлайки"],
      datasets: [
        {
          data: [70, 30],
          backgroundColor: ["#10B981", "#EF4444"],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
    },
  });
};

const createBarChart = () => {
  const ctx = document.getElementById("barChart").getContext("2d");
  barChart.value = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Отправленные", "Полученные"],
      datasets: [
        {
          label: "Лайки",
          data: [40, 60],
          backgroundColor: "rgba(75, 192, 192, 0.7)",
          borderWidth: 1,
        },
        {
          label: "Дизлайки",
          data: [20, 10],
          backgroundColor: "rgba(255, 99, 132, 0.7)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          stacked: true,
        },
        y: {
          stacked: true,
        },
      },
    },
  });
};
</script>

<template>
  <FooterNav />
  <div class="container">
    <div class="title">
      <span>Статистика</span>
    </div>

    <div class="text_statistic">
      <div class="elements like_send">
        <div class="action">
          <heart></heart>
        </div>
        <div class="info">
          <span class="text">Отправлено лайков</span>
          <span class="count">23</span>
        </div>
      </div>

      <div class="elements diskile_send">
        <div class="action_dislike">
          <dislike></dislike>
        </div>
        <div class="info">
          <span class="text">Отправлено дизлайков</span>
          <span class="count">23</span>
        </div>
      </div>
      <div class="elements like_receive">
        <div class="action">
          <heart></heart>
        </div>
        <div class="info">
          <span class="text">Получено лайков</span>
          <span class="count">23</span>
        </div>
      </div>

      <div class="elements dislike_receive">
        <div class="action_dislike">
          <dislike></dislike>
        </div>
        <div class="info">
          <span class="text">Отправлено дизлайков</span>
          <span class="count">23</span>
        </div>
      </div>
    </div>

    <div class="circle_chart">
      <span>Отправленные реакции</span>

      <div>
        <canvas id="pieChart"></canvas>
      </div>
    </div>

    <div class="bar_chart">
      <span>Сравнения</span>

      <div>
        <canvas id="barChart"></canvas>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
span {
  font-family: Arial, sans-serif;
}
.container {
  // margin-left: 5px;
  // padding-right: 10px; // Добавляем симметричный отступ
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;

  .title {
    margin: 40px 0 20px 0;
    color: black;
    font-weight: 700;
    font-size: 24px;
  }

  .text_statistic {
    
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 25px;
    box-sizing: border-box;

    .elements {
      height: auto;
    box-sizing: border-box;
    padding: 15px;
      background-color: white;
      width: 100%;
      min-height: 10vh;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      display: flex;
      align-items: center;
      font-size: 14px;
      color: #8a97a7;
      gap: 15px;

      border-radius: 20px;

      .info {
        display: flex;
        flex-direction: column;
        gap: 10px;

        .count {
          font-size: 20px;
          color: black;
          font-weight: 700;
        }
      }

      .action {
        background-color: #dcfce7;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px;
        // width: 5%;
      }
      .action_dislike {
        background-color: #fee2e2;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 8px;
        // width: 5%;
      }
    }
  }
  .circle_chart,
  .bar_chart {
    margin-top: 30px;
    padding: 15px;
    background-color: white;
    width: 97%;
    height: 38vh;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);

    border-radius: 20px;
    font-weight: 500;
    font-size: 1.125rem;
  }
}
</style>
