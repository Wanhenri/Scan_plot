RASCUNHO:

\documentclass[11pt]{article}
\usepackage[a4paper,left=3cm,right=3cm,top=2.5cm,bottom=2.5cm,headsep=0.5cm,includeheadfoot]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{parskip}
\usepackage{booktabs}

\usepackage{lmodern}
\usepackage{tabularx}
\usepackage{graphicx,grffile}
\usepackage[hidelinks]{hyperref}
\usepackage{subfig}
\usepackage{subfigure}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{xcolor}
\usepackage[hidelinks]{hyperref}
\usepackage{eso-pic}
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{mwe}
\usepackage{float}
\usepackage{csquotes}
\usepackage{setspace} 
\usepackage{fancyhdr}

\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amsfonts}

% this pads tables with some extra space for readability

\pagestyle{fancy}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\setlength\headheight{80.0pt}
\addtolength{\textheight}{-80.0pt}
\lhead{\includegraphics[height=1.5cm]{logo_alinhado.png}}
\rhead{}
\fancyfoot{}


\fancyfoot[R]{\thepage}

\definecolor{azulinpe}{RGB}{0,117,180}

\newcommand\textoendinpe{%
  \textcolor{azulinpe}{\footnotesize Sede: Av. dos Astronautas, 1758, 12227-010 São José dos Campos(SP) Brasil tel +55-12 3208 6000}}
\newcommand\notaendinpe{%
\begin{tikzpicture}[remember picture,overlay]
\node[anchor=south west,xshift=70pt,yshift=83pt] at (current page.south west) {\textoendinpe};
\end{tikzpicture}%
}


\setlength{\parindent}{0cm}


\begin{document}

\AddToShipoutPictureBG{%
    \notaendinpe
    \AtPageLowerLeft{% 
        \begin{tikzpicture}[remember picture,overlay]
        % angles
        \coordinate (pagesw) at (.12\paperwidth,.12\paperheight);
        \draw[azulinpe, line width=1pt] (pagesw) -- +(15.5,0) -- (pagesw) -- +(0,22.5);
        \end{tikzpicture}
    }
}


\begin{titlepage}
    \doublespacing
    \vspace*{-3cm}
    \begin{figure}[!ht]
    \includegraphics[height=1.5cm]{logo_alinhado.png}
\end{figure}
        
\vspace{3cm}
       
\begin{center}
    \large{\textbf{PCI/MCTI/INPE}}\\
    \large{\textbf{RELATÓRIO TÉCNICO DE ATIVIDADES}}\\
    \large{\textbf{(Referente ao período: ******}}
\end{center}
    
\vspace{3cm}
        
\begin{flushleft}
    \begin{tabbing}
        \textbf{Número do Processo Institucional: ******/****-*}\\
        \textbf{Número do Processo Individual: ******/****-*} \\
        \textbf{Bolsista: ******}\\
        \textbf{Supervisor: ******}\\
        \textbf{Colaborador: ******}\\
        \textbf{Área: ******}\\
        \textbf{Vigência original da bolsa: ******}\\
        \textbf{Modalidade da bolsa: ******}            
    \end{tabbing}
\end{flushleft}
\end{titlepage}
    
    
    
\begin{center}
    \large{\textbf{RELATÓRIO TÉCNICO DE ATIVIDADES}}\\
    \vspace{1cm}
    \large{\textbf{Validação do Modelo Atmosférico Global do CPTEC/INPE para Previsão Sazonal}}
\end{center}

\section{Histórico}

\newpage

\section{Resumo do Projeto}

\newpage

\section{Objetivos}

\newpage

\section{Atividades Desenvolvidas Durante o Período da Bolsa}

\subsection{Desenvolvimento das Atividades}

\newpage

\section{Resultados Obtidos em Função do Plano de Trabalho Proposto}


\newpage

\section{Conclusões Gerais}

\newpage


\end{document}


propósito 
Publico alvo
Escopo
Definições 
Visão geral do produto
Descrição dos usuários
modelo conceitual 
Modelagem relacional
caso de uso
prototipos
metodologia e cronograma
