# 🏨 Hotel Reservation Prediction

## 📌 Overview
This project aims to predict **hotel reservation outcomes** (such as whether a booking will be canceled or confirmed) based on customer and booking information.  
The model leverages machine learning to analyze reservation patterns and help hotels optimize occupancy, pricing, and customer service.

---

## 📊 Dataset Features
The dataset includes the following key features:

- **Name** → Guest name (identifier, not used in training).
- **No of Adults** → Number of adults in the booking.
- **No of Children** → Number of children in the booking.
- **No of Weekend Nights** → Nights stayed during weekends.
- **No of Week Nights** → Nights stayed during weekdays.
- **Type of Meal Plan** → Meal plan chosen by the customer.
- **Required Car Parking Space** → Number of parking spaces requested.
- **Room Type Reserved** → Type of room booked.
- **Lead Time** → Number of days between booking and arrival.
- **Arrival Year / Month / Date** → Booking arrival date.
- **Reservation Type** → Source of booking (e.g., Online, Corporate, Offline).
- **Repeated Guest** → Whether the guest has booked before.
- **No of Previous Cancellations** → Count of past cancellations.
- **No of Previous Bookings not canceled** → Count of past successful bookings.
- **Avg Price Per Room** → Average price per night for the reservation.
- **No of Special Requests** → Number of special requests made by the guest.

## 🖼️ Project Demo

![🏨 Hotel Reservation Prediction_demo](https://github.com/maskar122/Hotel-_Reservation/blob/e206bb5d612a9eba63ab39362abda2a61fabab89/images/Screenshot%20(297).png)

**Target Variable**:
- **Booking Status** → (e.g., `Canceled` or `Not Canceled`).

---

## 🛠️ Tech Stack
- **Python** (pandas, numpy, scikit-learn, matplotlib, seaborn)
- **Machine Learning Models**: Logistic Regression, Random Forest, XGBoost
- **Visualization**: Matplotlib, Seaborn
- **Deployment**: Streamlit / Flask (optional)

---

## 📈 Results

The model predicts whether a booking will be confirmed or canceled.

Key factors influencing cancellations:

High lead time (bookings made far in advance tend to cancel more).

Guests with a history of cancellations.

Very high or very low average price per room.

Few or no special requests.

