# Advanced Task Tree Generation for Robotic Cooking

**Project Title**:  
Advanced Task Tree Generation for Robotic Cooking using FOONs and LLMs

**Author**:  
Lokeshwar Reddy Yarava

---

## 🥘 Project Overview

Robotic systems often struggle to interpret natural language instructions for complex tasks like cooking. This project presents a novel approach that integrates **Large Language Models (LLMs)** with **Functional Object-Oriented Networks (FOONs)** to create structured task trees for robotic manipulation tasks.  
Our system improves task understanding, execution success, and enables human-robot collaboration.

---

## 🚀 Methodology

- **Functional Object-Oriented Network (FOON)**: Structured manipulation knowledge using objects, motions, and outcomes.
- **Prompt Engineering**:
  - **Chain of Thought Prompting**: (Best performance)
  - **Few-Shot Prompting**
  - **Zero-Shot Prompting**
- **Task Tree Generation**: Automatic generation of JSON-based task trees for dishes using Gemini LLM.
- **FOON Weighting**: Weights incorporated based on robot success rates to optimize task plans.
- **Human-Robot Collaboration**: For difficult steps, humans assist to maximize task success.

---

## 🛠️ Built With

- **Python 3.9+**
- **Google Gemini API (Generative AI)**
- **Functional Object-Oriented Networks (FOON)**
- **JSON for task tree output format**

---

## 📁 Project Structure

```
Robotic_Cooking_TaskTree/
├── code/
│   ├── gemini.py
│   ├── prompt.py
│   ├── input.json
│   ├── kitchen.txt
├── docs/
│   ├── Paper.pdf           # Conference paper
│   ├── REPORT.pdf          # Approach analysis report
├── README_COOKING_PROJECT.md
├── LICENSE                
├── .gitignore             

```

---

## ⚡ How to Run Locally

1. Install requirements
```bash
pip install google-generativeai Pillow
```

2. Set up `config.json` with your Gemini API key:
```json
{
  "key": "YOUR_API_KEY"
}
```

3. Run the generator:
```bash
python gemini.py
```

The task trees for each dish will be generated in separate JSON files.

---

## 📈 Results

| Prompting Approach | Task Tree Accuracy | Execution Success Rate |
| :----------------- | :----------------- | :--------------------- |
| Chain of Thought    | 92%                 | 88%                    |
| Few Shots           | 81%                 | 76%                    |
| Zero-Shot           | 74%                 | 69%                    |

✅ **Chain of Thought Prompting** proved to be the most effective!

---

## 🔥 Key Contributions

- Introduced **effective prompting** for LLM-driven robotic planning.
- Integrated **robot capability-aware FOONs**.
- Enabled **human-in-the-loop** assistance for critical steps.
- Produced a full **IEEE Conference style Paper** documenting methods and findings.

---

## 📚 References

- [Paulius et al., FOON: Functional Object-Oriented Network for Manipulation Learning](https://ieeexplore.ieee.org/document/7759413)
- [Sakib et al., Consolidating Trees of Robotic Plans Generated Using LLMs](https://arxiv.org/abs/2401.07868)

---

## 🧠 Future Work

- Incorporate multimodal inputs (images/videos).
- Extend to domains beyond cooking (e.g., healthcare, manufacturing).
- Explore prompt optimization and LLM fine-tuning for domain-specific tasks.

---

**Project Completed for**:  
Advanced Topics in Deep Learning - Spring 2025  
**Instructor**: Prof. Yu Sun  
University of South Florida
