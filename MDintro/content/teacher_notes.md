# MD 입문 · 강사용 노트

총 60분(휴식 없음). 각 실습 바로 다음 슬라이드에 정답·해설이 있으며, 이어서 2시간 실습을 진행합니다.

## 1. Molecular dynamics(MD) 입문 (0–2분)

1강에서 2ITY의 Met793 주사슬(backbone) N과 gefitinib N3 사이 거리를 2.670 Å로 재었습니다. 이 값은 PDB 파일에 담긴 좌표 한 set에서 잰 거리이며, 시간에 따라 어떻게 변하는지는 파일에 들어 있지 않습니다. 오늘은 같은 structure를 물속, 300 K 조건에 두고 atom이 움직이도록 계산하는 방법인 MD를 배웁니다. 이 1시간은 원리와 결과 읽는 법에 집중하고, 명령 실행과 그래프 작성은 이어지는 2시간 실습에서 합니다. 수식은 F = m·a 하나만 사용합니다.

[PDB2ITY] RCSB PDB 2ITY: EGFR kinase–gefitinib
https://www.rcsb.org/structure/2ITY
[YUN2007] Yun et al. (2007) EGFR kinase–gefitinib structure (2ITY) · Cancer Cell 11:217–227
https://doi.org/10.1016/j.ccr.2006.12.017

## 2. 오늘 1시간, 이어서 2시간 실습 (2–4분)

세 강의가 같은 structure를 서로 다른 질문으로 본다는 흐름을 확인합니다. 1강은 좌표를 읽었고 2강은 예측 좌표와 confidence를 읽었습니다. 오늘은 coordinates가 시간에 따라 바뀌는 기록인 trajectory를 읽는 법을 배웁니다. 실습 프로그램의 출력에는 temperature, pressure, density, RMSD 같은 영어 이름이 그대로 나오므로 슬라이드도 같은 이름을 씁니다. 실습 도구가 GROMACS가 아니어도 이름과 옵션만 달라지고 개념은 같습니다.



## 3. Protein은 여러 시간 척도에서 움직인다 (4–7분)

Henzler-Wildman과 Kern(2007) Fig. 1b를 단순화한 그림입니다. bond vibration은 fs, side chain의 회전(rotamer라 부르는 회전 상태 사이의 변화, methyl group 회전)은 ps–ns, loop motion은 ns에서 µs 쪽, domain motion은 µs–ms 또는 그보다 느린 범위에 놓입니다. 작은 local motion일수록 빠르고 큰 collective motion일수록 느리다는 경향만 기억하게 합니다. 막대 경계는 대략적이며 protein과 조건에 따라 달라지고 서로 겹칩니다. 음영은 100 ns simulation이 담는 시간 범위입니다. 빠른 운동은 이 안에서 여러 번 일어나지만 µs–ms 운동은 한 번도 일어나지 않을 수 있다는 점을 바로 뒤 실습과 연결합니다.

[HWK2007] Henzler-Wildman & Kern (2007) Dynamic personalities of proteins · Nature 450:964–972
https://doi.org/10.1038/nature06522

## 4. Force field: atom 사이의 force를 정하는 근사식 (7–10분)

force field는 atom 배치에 따른 potential energy를 계산하는 식과 parameter의 묶음입니다. 공유결합으로 이어진 atom 사이에는 bond length, bond angle, dihedral 항을 쓰고, 떨어진 atom 사이에는 van der Waals와 electrostatic 항을 씁니다. 1강에서 본 Leu718의 비극성 접촉은 주로 van der Waals 항으로 표현됩니다. AMBER·CHARMM 같은 force field에는 hydrogen bond만을 위한 항이 따로 없고, Met793의 hydrogen bond는 partial charge 사이의 electrostatic과 van der Waals 항으로 표현됩니다. parameter는 quantum-mechanical 계산과 실험 데이터에 맞춘 근사이므로 force field마다 결과가 조금씩 다를 수 있습니다. classical MD에서는 공유결합이 끊어지거나 새로 생기지 않으므로 화학 반응은 다루지 않습니다.

[HD2018] Hollingsworth & Dror (2018) Molecular Dynamics Simulation for All · Neuron 99:1129–1143
https://doi.org/10.1016/j.neuron.2018.08.011

## 5. MD의 기본 반복: force를 계산하고 조금 움직인다 (10–13분)

MD는 atom마다 위치와 속도를 가진 상태에서 시작합니다. force field로 모든 atom에 걸리는 force를 계산하고, Newton 법칙 F = m·a로 가속도를 구한 뒤 아주 짧은 time step만큼 위치와 속도를 갱신합니다. 이 과정을 수백만 번 이상 반복하고 일정 간격으로 좌표를 저장하면 frame이 쌓여 trajectory가 됩니다. time step은 가장 빠른 bond vibration을 놓치지 않도록 몇 fs로 잡습니다. 시작 velocities는 보통 목표 temperature에 맞춰 무작위로 정하므로 같은 structure에서 출발해도 trajectory마다 경로가 달라집니다. 이렇게 시작 velocities만 바꿔 되풀이한 계산을 replica라고 부르며, 이 점이 뒤에서 replica를 여러 번 돌려야 하는 이유가 됩니다.

[HD2018] Hollingsworth & Dror (2018) Molecular Dynamics Simulation for All · Neuron 99:1129–1143
https://doi.org/10.1016/j.neuron.2018.08.011
[GMX_TUT] GROMACS tutorials: Introduction to Molecular Dynamics
https://tutorials.gromacs.org/docs/md-intro-tutorial.html

## 6. 계산 상자 만들기: protein + water + ion (13–16분)

실제 계산 전에 system을 만듭니다. structure에 빠진 atom·residue가 있거나 hydrogen이 없으면 force field parameter를 붙일 수 없습니다. 2ITY처럼 약물이 있으면 ligand parameter를 따로 준비해야 합니다. Lemkul의 lysozyme 튜토리얼은 protein만 다루고, protein–ligand complex는 별도 튜토리얼에서 ligand parameter를 만듭니다. GROMACS 공식 튜토리얼은 protein을 가운데 두고 box 벽에서 1.0 nm 이상 띄웁니다. periodic boundary condition에서는 상자가 사방으로 복제되므로 이웃한 image 사이가 2.0 nm 이상이 되어 nonbonded cut-off(1.2 nm)보다 멀어지고, protein이 자기 복제본과 상호작용하지 않습니다. Lemkul 튜토리얼은 1.2 nm(image 사이 2.4 nm)를 씁니다. water model은 선택한 force field와 함께 쓰도록 만들어진 것을 고릅니다. 두 튜토리얼이 쓰는 spc216.gro는 SPC·SPC/E·TIP3P 같은 3-point water model에 함께 쓰는 좌표입니다. 마지막으로 Na⁺·Cl⁻를 넣어 전체 charge를 0으로 맞춥니다.

[GMX_TUT] GROMACS tutorials: Introduction to Molecular Dynamics
https://tutorials.gromacs.org/docs/md-intro-tutorial.html
[MDTUT] Lemkul: GROMACS Tutorials (Lysozyme in Water)
https://www.mdtutorials.com/gmx/
[LEMKUL2019] Lemkul (2019) From Proteins to Perturbed Hamiltonians: GROMACS tutorials · LiveCoMS 1:5068
https://doi.org/10.33011/livecoms.1.1.5068

## 7. NVT와 NPT: 계산 중 무엇을 일정하게 두나 (16–19분)

NVT와 NPT는 계산하는 동안 일정하게 유지하는 양의 머리글자입니다. N은 atom 수, V는 box 부피, T는 temperature, P는 pressure입니다. 튜토리얼은 이런 계산 조건을 ensemble이라고 부르며, NVT는 canonical(isothermal-isochoric), NPT는 isothermal-isobaric ensemble이라고도 합니다. 이 수업에서는 '무엇을 일정하게 두고 계산하는가'로 이해하면 충분합니다. MD에서 temperature는 atom들이 움직이는 빠르기, 즉 kinetic energy로부터 계산합니다. thermostat는 이 temperature가 목표값에 맞도록 atom velocities를 조정합니다. pressure는 atom의 움직임과 atom 사이 force로 계산하며, barostat는 평균 pressure가 목표값에 맞도록 box 크기를 조금씩 늘리거나 줄입니다. 그래서 NVT에서는 box 크기가 고정되고, NPT에서는 box 크기와 density가 변하다가 안정됩니다. 실험은 보통 일정한 온도와 압력에서 하므로 튜토리얼은 NPT가 실험 조건에 가장 가깝다고 설명합니다. 두 튜토리얼 모두 thermostat로 V-rescale, barostat로 C-rescale(stochastic cell rescaling)을 씁니다. 목표값은 GROMACS 공식 튜토리얼이 300 K, Lemkul 튜토리얼이 298 K와 1 bar입니다.

[GMX_TUT] GROMACS tutorials: Introduction to Molecular Dynamics
https://tutorials.gromacs.org/docs/md-intro-tutorial.html
[MDTUT] Lemkul: GROMACS Tutorials (Lysozyme in Water)
https://www.mdtutorials.com/gmx/

## 8. 준비 4단계: EM → NVT → NPT → production (19–23분)

튜토리얼 순서를 따라 네 단계를 설명합니다. EM은 시간을 진행시키지 않고 energy가 낮아지는 방향으로 좌표를 조정해 너무 가까운 접촉을 풉니다. Lemkul 튜토리얼은 potential energy가 음수이고 (물속의 작은 protein이라면) 크기가 10⁵–10⁶ 규모인지, 최대 force가 기준값(emtol) 아래로 내려왔는지 확인하게 합니다. NVT에서는 protein heavy atom에 position restraints를 걸고 temperature를 목표값에 맞춥니다. 목표값은 GROMACS 공식 튜토리얼이 300 K, Lemkul 튜토리얼이 298 K입니다. NPT에서는 restraints를 유지한 채 pressure를 1 bar에 맞추고 density가 안정되는지 봅니다. Lemkul 튜토리얼의 예에서 pressure 평균은 −3 ± 11 bar로 요동이 커서 1 bar와 통계적으로 구별되지 않으므로, density가 안정되었는지를 함께 봅니다. production에서는 restraints를 풀고 분석할 trajectory를 저장합니다. Lemkul 튜토리얼의 mdp는 NVT 100 ps, NPT 500 ps이며, 실습 자료의 mdp 값은 실습에서 직접 확인합니다.

[GMX_TUT] GROMACS tutorials: Introduction to Molecular Dynamics
https://tutorials.gromacs.org/docs/md-intro-tutorial.html
[MDTUT] Lemkul: GROMACS Tutorials (Lysozyme in Water)
https://www.mdtutorials.com/gmx/
[LEMKUL2019] Lemkul (2019) From Proteins to Perturbed Hamiltonians: GROMACS tutorials · LiveCoMS 1:5068
https://doi.org/10.33011/livecoms.1.1.5068

## 9. 바로 실습 ① · 계산 길이를 step 수로 바꾸기 (23–26분)

1분 동안 계산하고 1분 동안 옆 사람과 답을 맞춥니다. 1 ps = 1,000 fs이므로 100 ps는 100,000 fs입니다. 2번 문항은 3번 슬라이드의 시간 척도 그림을 다시 보며 답하게 합니다. 정답은 다음 슬라이드에 있습니다.

[MDTUT] Lemkul: GROMACS Tutorials (Lysozyme in Water)
https://www.mdtutorials.com/gmx/
[HWK2007] Henzler-Wildman & Kern (2007) Dynamic personalities of proteins · Nature 450:964–972
https://doi.org/10.1038/nature06522

## 10. 정답·해설 ① · 1 µs는 5억 step (26–28분)

Lemkul GROMACS 튜토리얼의 NVT 설정(nvt.mdp)은 nsteps = 50000, dt = 0.002 ps로 100 ps입니다. 같은 time step으로 1 µs를 계산하려면 5억 step이 필요합니다. step마다 모든 atom의 force를 다시 계산하므로 계산 길이는 컴퓨터 시간과 직접 연결됩니다. 100 ns simulation에서 domain motion이 보이지 않았다면 '없다'가 아니라 '이 길이에서는 관찰되지 않았다'고 써야 합니다. 느린 운동을 다루는 방법(더 긴 계산, 여러 replica, enhanced sampling)은 이름만 소개하고 넘어갑니다.

[MDTUT] Lemkul: GROMACS Tutorials (Lysozyme in Water)
https://www.mdtutorials.com/gmx/
[HWK2007] Henzler-Wildman & Kern (2007) Dynamic personalities of proteins · Nature 450:964–972
https://doi.org/10.1038/nature06522
[HD2018] Hollingsworth & Dror (2018) Molecular Dynamics Simulation for All · Neuron 99:1129–1143
https://doi.org/10.1016/j.neuron.2018.08.011

## 11. 왜 NVT 다음에 NPT인가? (28–30분)

두 튜토리얼 모두 equilibration을 두 단계로 나눕니다. volume을 고정한 NVT에서 thermostat로 temperature를 목표값에 맞춰 안정시킨 뒤, NPT에서 barostat가 box 크기를 조정해 pressure와 density를 안정시킵니다. 각 단계는 앞 단계의 마지막 상태를 checkpoint 파일로 이어받습니다(GROMACS grompp의 -t 옵션, mdp의 continuation = yes). Lemkul 튜토리얼은 EM 직후 restraints 없이 dynamics를 시작하면 system이 무너질 수 있다고 설명합니다. water는 자기들끼리는 최적화되어 있지만 protein 주변에는 아직 맞춰지지 않았기 때문입니다. 순서를 '먼저 temperature, 다음 pressure와 density'로 요약하게 합니다.

[MDTUT] Lemkul: GROMACS Tutorials (Lysozyme in Water)
https://www.mdtutorials.com/gmx/
[LEMKUL2019] Lemkul (2019) From Proteins to Perturbed Hamiltonians: GROMACS tutorials · LiveCoMS 1:5068
https://doi.org/10.33011/livecoms.1.1.5068
[GMX_TUT] GROMACS tutorials: Introduction to Molecular Dynamics
https://tutorials.gromacs.org/docs/md-intro-tutorial.html

## 12. 바로 실습 ② · 단계 순서와 확인 값 짝짓기 (30–32분)

섞어 놓은 단계와 확인 값을 연결하는 1분 활동입니다. 먼저 순서를 쓰게 하고, 다음으로 각 단계에서 어떤 그래프를 볼지 짝짓게 합니다. 실습에서는 단계가 끝날 때마다 이 값을 그래프로 확인한다고 알려 줍니다. 3번은 restraints가 무엇을 붙잡고 무엇을 자유롭게 두는지 말로 설명하게 합니다.

[MDTUT] Lemkul: GROMACS Tutorials (Lysozyme in Water)
https://www.mdtutorials.com/gmx/
[LEMKUL2019] Lemkul (2019) From Proteins to Perturbed Hamiltonians: GROMACS tutorials · LiveCoMS 1:5068
https://doi.org/10.33011/livecoms.1.1.5068

## 13. 정답·해설 ② · C → D → A → B (32–33분)

정답은 C(EM) → D(NVT) → A(NPT) → B(production)입니다. EM은 potential energy와 최대 force, NVT는 temperature, NPT는 pressure 평균과 density, production은 분석용 trajectory와 짝입니다. position restraints는 protein heavy atom을 시작 위치 근처에 붙잡아 두고 water와 ion이 주변에 먼저 자리 잡게 합니다. production에서는 restraints를 풀어야 protein 자체의 움직임을 관찰할 수 있습니다.

[MDTUT] Lemkul: GROMACS Tutorials (Lysozyme in Water)
https://www.mdtutorials.com/gmx/
[LEMKUL2019] Lemkul (2019) From Proteins to Perturbed Hamiltonians: GROMACS tutorials · LiveCoMS 1:5068
https://doi.org/10.33011/livecoms.1.1.5068

## 14. RMSD: 기준 structure에서 얼마나 달라졌나 (33–37분)

RMSD는 각 frame을 기준 structure에 least-squares fit으로 겹쳐 전체 이동과 회전을 없앤 뒤, 대응 atom 사이 거리의 제곱 평균의 제곱근을 구한 값입니다. GROMACS gmx rms는 fit에 쓰는 group과 RMSD를 계산하는 group을 따로 고를 수 있으므로, 예를 들어 backbone으로 겹치고 ligand의 RMSD를 볼 수 있습니다. 그래프는 가상 교육용 데이터입니다. replica 1과 2는 약 1.5–1.8 Å에서 평평하고, replica 3은 55 ns까지 비슷하다가 그 뒤 약 3 Å로 이동합니다. 평평한 RMSD는 기준 structure에 대해 안정했다는 뜻일 뿐이며, 서로 다른 conformation도 비슷한 RMSD를 가질 수 있어 수렴의 증거로는 부족합니다. GROMACS 출력 단위는 nm이므로 실습에서 0.15 nm = 1.5 Å로 바꿔 읽습니다.

[GMX_RMSD] GROMACS reference manual: Root mean square deviations in structure
https://manual.gromacs.org/current/reference-manual/analysis/rmsd.html
[GROSSFIELD2018] Grossfield et al. (2018) Uncertainty and sampling quality in molecular simulations · LiveCoMS 1:5067
https://doi.org/10.33011/livecoms.1.1.5067

## 15. RMSF: residue마다 얼마나 흔들렸나 (37–40분)

RMSF는 trajectory에서 각 atom 위치가 시간 평균 위치로부터 얼마나 벗어나는지를 나타내는 표준편차입니다. residue 단위로는 흔히 Cα나 residue 평균을 그립니다. 가상 그래프에서는 양 끝과 17–21번 loop가 크게 흔들립니다. gmx rmsf의 -oq 옵션은 B = (8π²/3)·RMSF² 식으로 B-factor 값을 계산해 PDB 파일의 B-factor 칸에 기록하므로, 1강에서 읽은 mmCIF의 B_iso_or_equiv와 같은 칸에서 비교할 수 있습니다. 다만 crystal B-factor에는 격자 안의 disorder와 모델링 오차도 섞여 있어 숫자가 그대로 같지는 않습니다. 2강의 pLDDT는 예측 structure의 local confidence이고, RMSF는 simulation 중 계산된 흔들림입니다. 두 값은 관련될 수 있어도 같은 양이 아닙니다.

[GMX_RMSF] GROMACS: gmx rmsf
https://manual.gromacs.org/current/onlinehelp/gmx-rmsf.html
[AF_CONF] EMBL-EBI: AlphaFold2 confidence scores (pLDDT · PAE)
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/

## 16. 거리와 H-bond: 한 장의 값에서 시간에 따른 분포로 (40–43분)

1강에서는 거리를 한 번 쟀지만, trajectory에서는 frame마다 같은 atom 쌍의 거리를 다시 잽니다. H-bond 판정에는 거리와 각도 기준이 필요합니다. donor와 acceptor는 1강에서 배운 수소결합의 주개와 받개입니다. GROMACS gmx hbond의 기본값은 donor–acceptor 거리 0.35 nm, hydrogen–donor–acceptor 각도 30°입니다. 기준을 만족한 frame의 비율이 occupancy입니다. 프로그램마다 기본 기준이 다르고 기준을 바꾸면 occupancy도 바뀌므로 결과와 함께 기준을 적게 합니다.

[GMX_HBOND] GROMACS 2025.1: gmx hbond
https://manual.gromacs.org/documentation/2025.1/onlinehelp/gmx-hbond.html
[PDB2ITY] RCSB PDB 2ITY: EGFR kinase–gefitinib
https://www.rcsb.org/structure/2ITY
[YUN2007] Yun et al. (2007) EGFR kinase–gefitinib structure (2ITY) · Cancer Cell 11:217–227
https://doi.org/10.1016/j.ccr.2006.12.017

## 17. 바로 실습 ③ · 10 frame으로 H-bond occupancy 계산 (43–46분)

화면의 가상 10 frame으로 계산합니다. 먼저 거리 기준만 적용하고, 다음으로 각도 기준을 함께 적용해 결과가 어떻게 달라지는지 봅니다. 3번은 1강의 '가깝다는 관찰과 강하게 결합한다는 결론은 다르다'를 떠올리게 합니다. 실제 2ITY simulation 결과가 아닌 교육용 값이며, 기준값과 정확히 같은 값은 넣지 않았습니다.

[GMX_HBOND] GROMACS 2025.1: gmx hbond
https://manual.gromacs.org/documentation/2025.1/onlinehelp/gmx-hbond.html

## 18. 정답·해설 ③ · 거리만 8/10, 각도까지 7/10 (46–48분)

거리 기준만 쓰면 frame 5(3.6 Å)와 7(4.2 Å)을 빼고 8 frame입니다. 각도까지 적용하면 frame 6이 3.0 Å이지만 35°여서 빠지므로 7/10, 70%입니다. occupancy는 접촉이 유지된 시간의 비율이지 결합 세기(affinity)가 아닙니다. 연속된 frame은 서로 비슷하므로 10 frame이 10개의 독립 관측은 아닙니다. Knapp 등(2018)은 trajectory 하나에서 본 차이가 통계적으로 유의해 보여도 다시 계산하면 재현되지 않을 수 있다고 보고했습니다. 같은 결론을 독립 replica에서 다시 확인하게 합니다.

[GMX_HBOND] GROMACS 2025.1: gmx hbond
https://manual.gromacs.org/documentation/2025.1/onlinehelp/gmx-hbond.html
[KNAPP2018] Knapp, Ospina & Deane (2018) The importance of replicas · J Chem Theory Comput 14:6127–6138
https://doi.org/10.1021/acs.jctc.8b00391

## 19. MD로 답할 수 있는 것과 한계 (48–51분)

MD의 강점과 한계를 짝지어 정리합니다. MD는 접촉, 거리, water 배치, 유연성이 시간에 따라 어떻게 변하는지 보여 주고 실험으로 확인할 가설을 만듭니다. 한계로는 force field 근사, 계산 길이보다 느린 운동, trajectory 하나의 우연성이 있습니다. Grossfield 등(2018)은 sampling이 충분한지를 관측량마다 따로 판단해야 한다고 권합니다. RMSD가 안정되어도 conformation 사이의 transition이나 population은 아직 수렴하지 않았을 수 있습니다. 2강에서 예측 후보의 비율 3/8을 equilibrium population으로 읽지 않았던 것처럼, MD에서 관찰한 frame 빈도도 충분한 sampling 근거 없이 population으로 읽지 않습니다.

[HD2018] Hollingsworth & Dror (2018) Molecular Dynamics Simulation for All · Neuron 99:1129–1143
https://doi.org/10.1016/j.neuron.2018.08.011
[KNAPP2018] Knapp, Ospina & Deane (2018) The importance of replicas · J Chem Theory Comput 14:6127–6138
https://doi.org/10.1021/acs.jctc.8b00391
[GROSSFIELD2018] Grossfield et al. (2018) Uncertainty and sampling quality in molecular simulations · LiveCoMS 1:5067
https://doi.org/10.33011/livecoms.1.1.5067

## 20. 최종 활동 · 세 주장을 근거에 맞게 고치기 (51–54분)

지금까지 배운 판단 기준을 적용하는 활동입니다. 각 주장에서 무엇을 관찰했는지와 무엇을 더 확인해야 하는지를 나누어 한 문장씩 고치게 합니다. 2분 작성 후 두세 명의 답을 듣고 다음 슬라이드로 정리합니다.

[GROSSFIELD2018] Grossfield et al. (2018) Uncertainty and sampling quality in molecular simulations · LiveCoMS 1:5067
https://doi.org/10.33011/livecoms.1.1.5067
[HWK2007] Henzler-Wildman & Kern (2007) Dynamic personalities of proteins · Nature 450:964–972
https://doi.org/10.1038/nature06522

## 21. 정답·해설 · 관찰한 만큼만 말하기 (54–57분)

첫째, 평평한 RMSD는 기준 structure에 대한 안정성만 말해 줍니다. 수렴을 주장하려면 독립 replica를 비교하고 관심 있는 관측량이 replica 사이에 일치하는지 확인해야 합니다. 둘째, occupancy는 접촉이 유지된 빈도이며 결합 세기는 결합 실험이나 별도의 free energy 계산으로 따져야 합니다. 셋째, µs–ms 운동은 100 ns 계산으로 부정할 수 없습니다. 좋은 설명은 관찰한 양, 계산 조건, 한계를 함께 적습니다.

[GROSSFIELD2018] Grossfield et al. (2018) Uncertainty and sampling quality in molecular simulations · LiveCoMS 1:5067
https://doi.org/10.33011/livecoms.1.1.5067
[KNAPP2018] Knapp, Ospina & Deane (2018) The importance of replicas · J Chem Theory Comput 14:6127–6138
https://doi.org/10.1021/acs.jctc.8b00391
[HWK2007] Henzler-Wildman & Kern (2007) Dynamic personalities of proteins · Nature 450:964–972
https://doi.org/10.1038/nature06522

## 22. 이제 2시간 실습으로 (57–59분)

실습 순서를 오늘 슬라이드 번호와 연결해 둡니다. 실습 중 막히면 해당 번호의 슬라이드를 다시 보게 합니다. 모든 결과에는 force field, water model, temperature, 계산 길이, replica 수, 분석 기준을 기록하게 합니다. 이 기록이 있어야 다른 사람이 결과를 재현하고 비교할 수 있습니다.

[GMX_TUT] GROMACS tutorials: Introduction to Molecular Dynamics
https://tutorials.gromacs.org/docs/md-intro-tutorial.html
[MDTUT] Lemkul: GROMACS Tutorials (Lysozyme in Water)
https://www.mdtutorials.com/gmx/

## 23. 참고 자료 (59–60분)

주요 출처입니다. Hollingsworth & Dror(2018)는 생물학 연구자를 위한 MD 입문 리뷰이고, Lemkul 튜토리얼과 GROMACS 튜토리얼은 실습 절차의 근거입니다. RMSD·RMSF·H-bond 정의는 GROMACS 공식 문서를 따랐습니다. 반복 실행과 sampling 판단은 Knapp 등(2018), Grossfield 등(2018)을 참고했습니다.

[HD2018] Hollingsworth & Dror (2018) Molecular Dynamics Simulation for All · Neuron 99:1129–1143
https://doi.org/10.1016/j.neuron.2018.08.011
[HWK2007] Henzler-Wildman & Kern (2007) Dynamic personalities of proteins · Nature 450:964–972
https://doi.org/10.1038/nature06522
[LEMKUL2019] Lemkul (2019) From Proteins to Perturbed Hamiltonians: GROMACS tutorials · LiveCoMS 1:5068
https://doi.org/10.33011/livecoms.1.1.5068
[MDTUT] Lemkul: GROMACS Tutorials (Lysozyme in Water)
https://www.mdtutorials.com/gmx/
[GMX_TUT] GROMACS tutorials: Introduction to Molecular Dynamics
https://tutorials.gromacs.org/docs/md-intro-tutorial.html
[GMX_RMSD] GROMACS reference manual: Root mean square deviations in structure
https://manual.gromacs.org/current/reference-manual/analysis/rmsd.html
[GMX_RMSF] GROMACS: gmx rmsf
https://manual.gromacs.org/current/onlinehelp/gmx-rmsf.html
[GMX_HBOND] GROMACS 2025.1: gmx hbond
https://manual.gromacs.org/documentation/2025.1/onlinehelp/gmx-hbond.html
[GROSSFIELD2018] Grossfield et al. (2018) Uncertainty and sampling quality in molecular simulations · LiveCoMS 1:5067
https://doi.org/10.33011/livecoms.1.1.5067
[KNAPP2018] Knapp, Ospina & Deane (2018) The importance of replicas · J Chem Theory Comput 14:6127–6138
https://doi.org/10.1021/acs.jctc.8b00391
[AF_CONF] EMBL-EBI: AlphaFold2 confidence scores (pLDDT · PAE)
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/
[YUN2007] Yun et al. (2007) EGFR kinase–gefitinib structure (2ITY) · Cancer Cell 11:217–227
https://doi.org/10.1016/j.ccr.2006.12.017
