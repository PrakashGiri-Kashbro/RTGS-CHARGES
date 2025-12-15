// Flutter app (single-file) for Android & iOS
// Calculates charges based on the Excel formula:
// =IF(A4<=100000,35,IF(A4>=1000000,MAX(A4*0.00174694109258516,2000),A4*0.0019960091082926))

import 'package:flutter/material.dart';

void main() {
  runApp(const ChargeCalculatorApp());
}

class ChargeCalculatorApp extends StatelessWidget {
  const ChargeCalculatorApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Charge Calculator',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const CalculatorScreen(),
    );
  }
}

class CalculatorScreen extends StatefulWidget {
  const CalculatorScreen({super.key});

  @override
  State<CalculatorScreen> createState() => _CalculatorScreenState();
}

class _CalculatorScreenState extends State<CalculatorScreen> {
  final TextEditingController _amountController = TextEditingController();
  double? charge;

  double calculateCharge(double amount) {
    if (amount <= 100000) {
      return 35.0;
    } else if (amount >= 1000000) {
      double calculated = amount * 0.00174694109258516;
      return calculated < 2000 ? 2000 : calculated;
    } else {
      return amount * 0.0019960091082926;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Charge Calculator'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'Enter Amount',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: _amountController,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'e.g. 250000',
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                double? amount = double.tryParse(_amountController.text);
                if (amount != null) {
                  setState(() {
                    charge = calculateCharge(amount);
                  });
                }
              },
              child: const Text('Calculate'),
            ),
            const SizedBox(height: 30),
            if (charge != null)
              Card(
                elevation: 4,
                child: Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: Column(
                    children: [
                      const Text(
                        'Calculated Charge',
                        style: TextStyle(fontSize: 16),
                      ),
                      const SizedBox(height: 10),
                      Text(
                        'Nu. ${charge!.toStringAsFixed(2)}',
                        style: const TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
          ],
        ),
      ),
    );
  }
}
